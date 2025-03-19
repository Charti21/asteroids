import pygame # type: ignore
import sys
from constants import *
from player import Player  #importing Player Class 
from asteroid import Asteroid
from asteroid import Shot
from asteroidfield import AsteroidField


def main() :
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #Setup the screen dimensions/window size
    Clock = pygame.time.Clock() #Create a Clock Instance
    dt = 0

    print("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")
    
    
   
    updateable = pygame.sprite.Group()    #
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (updateable, shots, drawable) #creating containers for shot method
    Player.containers = (updateable, drawable)


    AsteroidField() #Creating the asteroid field instance, enabling asteroids to spawn on edges of screen

    player = Player(x=SCREEN_WIDTH / 2 , y=SCREEN_HEIGHT / 2) #initializing player in the center of the screen
    

    while True :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        updateable.update(dt)

        for a in asteroids :
            if player.collision(a) :   #Use player and check for collision between player and asteroid, if so... game over!
                print ("Game over!")   
                sys.exit()   #exit the program
            for bullet in shots:
                if a.collision(bullet) : #If asteroid collides with a shot/bullet
                    a.split()        #split the asteroid when bullet hits it
                    bullet.kill()    #bullet disappears when hits an asteroid

    

        for item in drawable :   #Drawing all of the updates on the screen input declared earlier before exiting each game loop. 
                                #Has to be after the screen is filled black, and before pygame.display.flip() declared
            item.draw(screen)

        
        pygame.display.flip()     #
        
        dt = (Clock.tick(60) / 1000) #limiting how often the screen updates to a set factor of 60 FPS... in other words the game only updates 60 times per second.

if __name__ == "__main__" :
    main()