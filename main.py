#Importing needed packages
import pygame
#Let user know the game is loading
print("Initialising...")
#Initialising the pygame library
pygame.init()
#Set Display resolution
gameDisplay = pygame.display.set_mode((800,600))
#set window name
pygame.display.set_caption('Stick War')
#Definitions
clock = pygame.time.Clock()
crashed = False
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