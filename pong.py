import random
import pygame

# Setup
pygame.init()
WIDTH, HEIGHT = 1440, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
font = pygame.font.Font(None, 300)
font_size = font.size("10")

bg_color = (120, 120, 255)
MID_FIELD = (WIDTH // 2, HEIGHT // 2)
POINTS_FACTOR = 5

# Ball setup
BALL_RADIUS = 20
BALL_COLOR = (200, 50, 50)
abs_speed = 300
ball_speed = (random.choice([-1, 1]) * abs_speed, random.choice([-1, 1]) * abs_speed)
ball_x = BALL_START_X = MID_FIELD[0]
ball_y = BALL_START_Y = MID_FIELD[1]

# Paddle setup
PADDLE_WIDTH = 20
PADDLE_HEIGHT = 100
PADDLE_COLOR = (255, 255, 255)
PADDLE_SPEED = 80
PADDLE_MARGIN_X = 20
PADDLE_BOUNDARY_CORRECTION = 10

# Colors
POINTS_COLOR = (255, 255, 255)
LINE_COLOR = (255, 255, 255)
level_change = 0

mid_paddle_y = MID_FIELD[1] - PADDLE_HEIGHT // 2
paddle1_x = PADDLE_MARGIN_X
paddle1_y = mid_paddle_y
paddle1_speed = PADDLE_SPEED
paddle1_points = 0
paddle1_height = PADDLE_HEIGHT
p1_pos = (MID_FIELD[0] - font_size[0] - 20, MID_FIELD[1] - font_size[1] // 2)
p1_level_change  = 1

paddle2_x = WIDTH - PADDLE_WIDTH - PADDLE_MARGIN_X
paddle2_y = mid_paddle_y
paddle2_speed = PADDLE_SPEED
paddle2_points = 0
paddle2_height = PADDLE_HEIGHT
p2_pos = (MID_FIELD[0] + (font_size[0] // 2 + 20), MID_FIELD[1] - font_size[1] // 2)
p2_level_change  = 1
line_pos = (WIDTH // 2, 0, 5, HEIGHT)

# Function to reset ball position
def reset_ball():
    return (random.choice([-1, 1]) * abs(ball_speed[0]), 
            random.choice([-1, 1]) * abs(ball_speed[1]))

while True:
    dt = pygame.time.Clock().tick(60) / 1000
    screen.fill(bg_color)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_y -= paddle1_speed * dt
        
    if keys[pygame.K_s]:
        paddle1_y += paddle1_speed * dt

    if keys[pygame.K_UP]:
        paddle2_y -= paddle2_speed * dt
    if keys[pygame.K_DOWN]:
        paddle2_y += paddle2_speed * dt

    # Check ball collision with walls
    if ball_y - BALL_RADIUS <= 0:
        ball_y = BALL_RADIUS + 1
        ball_speed = (ball_speed[0], -ball_speed[1])
    if ball_y + BALL_RADIUS >= HEIGHT:
        ball_y = HEIGHT - BALL_RADIUS - 1
        ball_speed = (ball_speed[0], -ball_speed[1])


    # Check if ball is out of bounds and update points
    if ball_x - BALL_RADIUS <= 0:
        paddle2_points += 1
        ball_speed = reset_ball()
        ball_x = BALL_START_X
        ball_y = BALL_START_Y
        
    if ball_x + BALL_RADIUS >= WIDTH:
        paddle1_points += 1
        ball_speed = reset_ball()
        ball_x = BALL_START_X
        ball_y = BALL_START_Y

    # Track total points for level ups
    total_points = paddle1_points + paddle2_points

    # Game level up
    # Paddles level up
    if  paddle1_points > 0 and paddle1_points % POINTS_FACTOR == 0 and p1_level_change != paddle1_points:
        paddle1_height += 20
        p1_level_change = paddle1_points

    if paddle2_points > 0 and paddle2_points % POINTS_FACTOR == 0 and p2_level_change != paddle2_points:
        paddle2_height += 20
        p2_level_change = paddle2_points

    # Ball level up
    if total_points > 0 and total_points % POINTS_FACTOR == 0 and level_change != total_points:
        ball_speed = (ball_speed[0] * 1.2, ball_speed[1] * 1.2)
        bg_color = (random.randint(0, 
        255), random.randint(0, 255), random.randint(0, 255))
        level_change = total_points   

    # Update ball position
    ball_x += ball_speed[0] * dt
    ball_y += ball_speed[1] * dt

    # Prevent paddles from going out of bounds
    if paddle1_y < 0:
        paddle1_y += PADDLE_BOUNDARY_CORRECTION

    if paddle1_y + paddle1_height >= HEIGHT:
        paddle1_y -= PADDLE_BOUNDARY_CORRECTION
    
    if paddle2_y < 0:
        paddle2_y += PADDLE_BOUNDARY_CORRECTION

    if paddle2_y + paddle2_height >= HEIGHT:
        paddle2_y -= PADDLE_BOUNDARY_CORRECTION

    # Draw paddles, ball, and points
    line_rect = pygame.draw.rect(screen, LINE_COLOR, line_pos)

    p1_points_rect = font.render(str(paddle1_points), True, POINTS_COLOR)
    screen.blit(p1_points_rect, p1_pos)
    p2_points_rect = font.render(str(paddle2_points), True, POINTS_COLOR)
    screen.blit(p2_points_rect, p2_pos)

    ball_rect = pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    paddle1_rect = pygame.draw.rect(screen, PADDLE_COLOR, (paddle1_x, paddle1_y, PADDLE_WIDTH, paddle1_height))
    paddle2_rect = pygame.draw.rect(screen, PADDLE_COLOR, (paddle2_x, paddle2_y, PADDLE_WIDTH, paddle2_height))
    
    # Handle ball collision with paddles
    if ball_rect.colliderect(paddle1_rect) or ball_rect.colliderect(paddle2_rect):
        ball_speed = (-ball_speed[0], ball_speed[1])

    pygame.display.flip()