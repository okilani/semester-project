import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
light_brown = (190, 133, 63)

# Main game loop (making the background color)
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with brown color
    screen.fill(light_brown)

    # Countdown variables
    countdown_seconds = 60
    clock = pygame.time.Clock()

    # Main loop
    while countdown_seconds > 0:
        # Calculate remaining time
        countdown_seconds -= clock.tick_busy_loop(60) / 1000  # Subtract elapsed time

        # Render and display the countdown timer at the top-middle
        font = pygame.font.Font(None, 30)  # Move font creation inside the loop
        countdown_text = font.render(f"Time Left: {int(countdown_seconds)}", True, (0, 0, 0))
        text_rect = countdown_text.get_rect(center=(screen_width // 2, 50))  # Center the text horizontally
        screen.blit(countdown_text, text_rect)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

    # Additional action after countdown completes (if needed)
    print("Countdown finished!")


# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))


# Define colors
red = (255, 0, 0)
white = (255, 255, 255)

# Set up the target parameters
target_radius = 50
center = (width // 2, height // 2)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear the screen
    screen.fill(white)

    # Draw the target
    pygame.draw.circle(screen, red, center, target_radius)
    pygame.draw.circle(screen, white, center, target_radius // 2)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)