import pygame
import random
import sys
import tkinter as tk 
import math
import time

pygame.init()
font = pygame.font.Font(None, 40)

# Set up the screen dimensions
screen_width = 600
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
light_blue = (173, 216, 230)
target_color = (255, 0, 0)  # Red color for the target
black = (0, 0, 0)
white = (255, 255, 255)
#getting cords for the first random circle 
target_x = random.randint(25, screen_width - 25)
target_y = random.randint(25, screen_height - 25)
target_radius = 25
target_spawn = (target_x, target_y)

#Reaction time test 
def on_button_click1(): 
  #removing buttons  
  button.destroy()
  button2.destroy()
  #removing tk window 
  root.destroy()  
  # Initialize Pygame
  pygame.init()
  
  # Fill the screen with blue color
  screen = pygame.display.set_mode((screen_width, screen_height))
  screen.fill(light_blue) 

#Full game 
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

# Initialize mouse coordinates
mouse_x, mouse_y = 0, 0
#creating the variable 
distance = None  
# Main game loop
running = True
create_new_circle = False  # Flag to control new circle creation

# Set up countdown variables
countdown_seconds = 60
clock = pygame.time.Clock()

#create the score 
score = 0 
# Main game loop
running = True
while running and countdown_seconds > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



  # Fill the top-right corner with blue color
    box_size = 45
    top_right_rect = pygame.Rect(screen_width - box_size, 0, box_size, box_size)
    pygame.draw.rect(screen, light_blue, top_right_rect)
    
  
    # Display the countdown at the top right
    text = font.render(str(countdown_seconds), True, black)
    text_rect = text.get_rect(topright=(screen_width - 10, 10))
    screen.blit(text, text_rect)

  # Display the score at the top left
    text = font.render(f"Score: {score}", True, black)
    text_rect = text.get_rect(topleft=(10, 10))
    screen.blit(text, text_rect)

  # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(1)

    # Decrement the countdown
    countdown_seconds -= 1

    # circle spawning and stuff 

  # Draw the target circle
    pygame.draw.circle(screen, target_color, target_spawn, target_radius)
    pygame.draw.circle(screen, black, target_spawn, target_radius, 2) 
  # Outline the circle in black

  # Update the display
    pygame.display.flip() 

    if event.type == pygame.MOUSEBUTTONDOWN:  # Check for mouse button click
        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
        # Perform actions based on mouse click position

        distance = math.sqrt((mouse_x - target_x)**2 + (mouse_y - target_y)**2)
        print(distance)
        print(target_radius)
        print(target_x) 
        print(target_y)
        print(mouse_x) 
        print(mouse_y)
        print(create_new_circle)
        target_radius = 25
        if distance <= target_radius:  
          create_new_circle = True 
        if create_new_circle == True:  # if click is within the circle and flag is True
          
          
          for i in range(1):
            #increase score by 1 
            score +=1
            # Remove circle by making everything blue 
            screen.fill(light_blue) 
            # Make new circle somewhere
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
            create_new_circle = False  # Reset the flag


# Function to display message
def display_message(message, color):
    text = font.render(message, True, color)
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))
    screen.blit(text, text_rect)
    pygame.display.flip()

#clear everything 
screen.fill(light_blue)

#giving the reaction time speed 
if countdown_seconds == 0:  # if game ends 
  if 10 >= score > 0:
      display_message("Your reaction time is HORRIBLE ", white)
  if 20 >= score > 10:
      # Do something for this score range
    display_message("Your reaction time is BELOW AVERGAGE ", white)
  if 30 >= score > 20:
      # Do something for this score range
    display_message("Your reaction time is  AVERGAGE ", white)
  if 40 >= score > 30:
      # Do something for this score range
    display_message("Your reaction time is ABOVE AVERGAGE ", white)
  if 50 >= score > 40:
      # Do something for this score range
    display_message("Your reaction time is CRAZY ", white)
  if 60 >= score > 50:
      # Do something for this score range
    display_message("Your reaction time is INSANE ", white)

    
# Wait for a few seconds before quitting
pygame.time.delay(10000)
# Quit Pygame properly
pygame.quit()
sys.exit()