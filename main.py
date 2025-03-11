# this allows us to use code from
# the open source pygame library
# throughout the file

import pygame # type: ignore
from constants import *
from player import Player  #importing Player Class from player.py file
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    Clock = pygame.time.Clock() #Create a Clock Instance
    dt = 0

    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    
    
   
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    player = Player(x=SCREEN_WIDTH / 2 , y=SCREEN_HEIGHT / 2) #initializing player in the center of the screen
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField() #Creating the asteroid instance
    
    

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        updateable.update(dt)
        

        for item in drawable :
            item.draw(screen)
        
        pygame.display.flip()
        #limit FPS to 60
        dt = (Clock.tick(60) / 1000)

if __name__ == "__main__" :
    main()