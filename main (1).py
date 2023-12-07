
import pygame
import random
import sys
import tkinter as tk 
# Initialize Pygame
pygame.init()

# Set up the screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
light_brown = (100, 133, 63)
target_color = (255, 0, 0)  # Red color for the target
black = (0, 0, 0)


def on_button_click1():#Reaction time test 
  button.destroy()
  button2.destroy()
  #removing tk window 
  root.destroy()
  # Initialize Pygame
  pygame.init()
  # Fill the screen with brown color
  screen = pygame.display.set_mode((screen_width, screen_height))
  screen.fill(light_brown)  
  
  # Where the target will randomly spawn 

  target_x = random.randint(25, screen_width - 25)
  target_y = random.randint(25, screen_height - 25)
  target_radius = 25
  target_spawn = (target_x, target_y)

  # Draw the target circle
  pygame.draw.circle(screen, target_color, target_spawn, target_radius)
  pygame.draw.circle(screen, black, target_spawn, target_radius, 2) 
  # Outline the circle in black

  # Update the display
  pygame.display.flip() 
  
def on_button_click2():#Full Game
  print("Full Game button clicked!")  # Action for Full Game button
  
root = tk.Tk()

# Button sizes
button_width = 12
button_height = 12
height = 163 
# Reaction time test button
button = tk.Button(root, text="Reaction time test", command=on_button_click1, width=button_width, height=button_height)
button.place(x=277, y=height)

# Full Game button
button2 = tk.Button(root, text="Full Game", command=on_button_click2, width=button_width, height=button_height)
button2.place(x=153, y=height)

root.mainloop()


# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
  
    if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button click
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
        # Perform actions based on mouse click position
        # ... 
  
    
# Quit Pygame properly
pygame.quit()
sys.exit()