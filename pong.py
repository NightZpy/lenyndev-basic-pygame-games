import random
import pygame

pygame.init()
WIDTH, HEIGHT = 1440, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
font = pygame.font.Font(None, 300)
font_size = font.size("10")

bg_color = (120, 120, 255)
MID_FIELD = (WIDTH // 2, HEIGHT // 2)
POINTS_FACTOR = 5

BALL_RADIUS = 20
BALL_COLOR = (200, 50, 50)
abs_speed = 300
ball_speed = (random.choice([-1, 1]) * abs_speed, random.choice([-1, 1]) * abs_speed)
ball_x = WIDTH // 2
ball_y = HEIGHT // 2

paddle_width = 20
paddle_color = (255, 255, 255)
points_color = (255, 255, 255)
level_change = 0

mid_paddle_y = MID_FIELD[1] - 100 // 2
paddle1_x = 20
paddle1_y = mid_paddle_y
paddle1_speed = 80
paddle1_points = 0
paddle1_height = 100
p1_pos = (MID_FIELD[0] - font_size[0] - 20, MID_FIELD[1] - font_size[1] // 2)
p1_level_change  = 1

paddle2_x = WIDTH - paddle_width - 20
paddle2_y = mid_paddle_y
paddle2_speed = 80
paddle2_points = 0
paddle2_height = 100
p2_pos = (MID_FIELD[0] + (font_size[0] // 2 + 20), MID_FIELD[1] - font_size[1] // 2)
p2_level_change  = 1

line_pos = (WIDTH // 2, 0, 5, HEIGHT)
line_color = (255, 255, 255)

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

    if ball_x - BALL_RADIUS <= 0:
        paddle2_points += 1
        ball_speed = (random.choice([-1, 1]) * ball_speed[0], random.choice([-1, 1]) * ball_speed[1])
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # Check if ball is out of bounds and update points    
    if ball_x + BALL_RADIUS >= WIDTH:
        paddle1_points += 1
        ball_speed = (random.choice([-1, 1]) * ball_speed[0], random.choice([-1, 1]) * ball_speed[1])
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2

    # Game level up
    # Paddles level up
    if  paddle1_points > 0 and paddle1_points % POINTS_FACTOR == 0 and p1_level_change != paddle1_points:
        paddle1_height += 20
        p1_level_change = paddle1_points

    if paddle2_points > 0 and paddle2_points % POINTS_FACTOR == 0 and p2_level_change != paddle2_points:
        paddle2_height += 20
        p2_level_change = paddle2_points

    # Ball level up
    if (paddle1_points + paddle2_points) > 0 and (paddle1_points + paddle2_points)  % POINTS_FACTOR == 0 and level_change != (paddle1_points + paddle2_points):
        ball_speed = (ball_speed[0] * 1.2, ball_speed[1] * 1.2)
        bg_color = (random.randint(0, 
        255), random.randint(0, 255), random.randint(0, 255))
        level_change = paddle1_points + paddle2_points   
        print("Level up!")
        print("Ball speed:", ball_speed)

    # Update ball position
    ball_x += ball_speed[0] * dt
    ball_y += ball_speed[1] * dt

    # Prevent paddles from going out of bounds
    if paddle1_y < 0:
        paddle1_y += 10

    if paddle1_y + paddle1_height >= HEIGHT:
        paddle1_y -= 10
    
    if paddle2_y < 0:
        paddle2_y += 10

    if paddle2_y + paddle2_height >= HEIGHT:
        paddle2_y -= 10

    # Draw paddles, ball, and points
    line_rect = pygame.draw.rect(screen, line_color, line_pos)

    p1_points_rect = font.render(str(paddle1_points), True, points_color)
    screen.blit(p1_points_rect, p1_pos)
    p2_points_rect = font.render(str(paddle2_points), True, points_color)
    screen.blit(p2_points_rect, p2_pos)

    ball_rect = pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)
    paddle1_rect = pygame.draw.rect(screen, paddle_color, (paddle1_x, paddle1_y, paddle_width, paddle1_height))
    paddle2_rect = pygame.draw.rect(screen, paddle_color, (paddle2_x, paddle2_y, paddle_width, paddle2_height))
    if ball_rect.colliderect(paddle1_rect):
        ball_speed = (-ball_speed[0], ball_speed[1])

    if ball_rect.colliderect(paddle2_rect):
        ball_speed = (-ball_speed[0], ball_speed[1])

    pygame.display.flip()