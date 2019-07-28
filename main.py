#Importing needed packages
import pygame
#Let user know the game is loading
print("Initialising...")
#Initialising the pygame library
pygame.init()
#Set Display parameters
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
#set window name
pygame.display.set_caption('Profiteer')
#Variables
clock = pygame.time.Clock()
crashed = False
black = (0,0,0)
white = (255,255,255)
#Game Loop
while not crashed:
    for event in pygame.event.get():
        #If the program needs to close
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()