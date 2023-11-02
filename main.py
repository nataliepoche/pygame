import pygame
import random # for color changes
import sys # stands for system if system closes

pygame.init() # Configures the project for you to run

screen = pygame.display.set_mode((800, 600)) # creates the height and width of screen
pygame.display.set_caption("The best game ever") # Creates name of the game

x_coordinate = 500 # sets coordinate for rectange
y_coodrinate = 300 # sets cordinate for rextange

running = True # must have a variable like this

while running == True:
    for event in pygame.event.get(): # Goes through the package and then goes to the events it has
        pygame.draw.rect(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), (x_coordinate, y_coodrinate, 50, 50))  # draws many shapes for you
    if event.type == pygame.QUIT:
        break

    button = pygame.key.get_pressed() # checks what kind of buttons on the keyboard does the user use, tracks the buttons pushed
    # creates different actions when a user presses a button
    print(x_coordinate, y_coodrinate)
    if button[pygame.K_LEFT]:
        x_coordinate -= 1 # moves coordinate to the left
    if button[pygame.K_RIGHT]:
        x_coordinate += 1 # moves coordinate to the right
    if button[pygame.K_UP]:
        y_coodrinate -= 1 # moves coordinate up
    if button[pygame.K_DOWN]:
        y_coodrinate += 1 # moves coordinate down
    if x_coordinate < 0:
        x_coordinate = 0 # resets coordinate to not go out of bounds
    if y_coodrinate < 0:
        y_coodrinate = 0

    pygame.time.Clock().tick(60)  # changes the tick rate of clock to be 60 ticks per section, creates a smoother experience, can be placed anywhere
    pygame.display.flip() # updates changes