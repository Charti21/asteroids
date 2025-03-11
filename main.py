# this allows us to use code from
# the open source pygame library
# throughout the file

import pygame
from constants import *

def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    Clock = pygame.time.Clock() #Create a Clock Instance
    dt = 0
    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        pygame.display.flip()
        Clock.tick(60)
        dt = (Clock.tick(60) / 1000)
    
    
if __name__ == "__main__" :
    main()