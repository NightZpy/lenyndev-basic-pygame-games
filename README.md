# 2D Game Development 101

This repository contains game development projects created as part of the gamedev_101 course.

## Pong Game

A simple implementation of the classic Pong game using Python and Pygame.

### Requirements

- Python 3.6 or higher
- Pygame

### Setup Instructions

#### 1. Setting up a Virtual Environment

It's recommended to use a virtual environment to avoid conflicts with other projects. To create a virtual environment:

```bash
# Navigate to the project directory
cd /path/to/project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

#### 2. Installing Dependencies

Once the virtual environment is activated, install the required packages:

```bash
# Install directly with pip
pip install pygame

# Or use the requirements.txt if available
pip install -r requirements.txt
```

#### 3. Running the Game

After installing the dependencies, you can run the game with:

```bash
python pong.py
```

### How to Play

- Player 1 (Left): Use 'W' and 'S' keys to move up and down
- Player 2 (Right): Use 'UP' and 'DOWN' arrow keys to move up and down
- The game gets progressively more challenging as players score points

## Credits

This code was developed as part of the programming courses by [@lenyndev](https://www.youtube.com/@lenyndev) on YouTube.

The Pong game specifically was explained in detail in this tutorial:
[Python Game Development - Creating Pong Game](https://www.youtube.com/live/VgzQ8gPaCiM?si=ILejM9Kl806PWI5N)

Check out more tutorials and courses on the [Lenyn Dev YouTube Channel](https://www.youtube.com/@lenyndev).
