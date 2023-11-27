import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Simple Game')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height - player_height - 10
player_speed = 5

# Set up the obstacle
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, window_width - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3

clock = pygame.time.Clock()

game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < window_width - player_width:
        player_x += player_speed

    # Update the obstacle position
    obstacle_y += obstacle_speed
    if obstacle_y > window_height:
        obstacle_x = random.randint(0, window_width - obstacle_width)
        obstacle_y = -obstacle_height

    # Check for collision
    if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x \
            and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
        game_over = True

    # Fill the window with the background color
    window.fill(BLACK)

    # Draw the player
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_width, player_height))

    # Draw the obstacle
    pygame.draw.rect(window, WHITE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Update the display
    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()