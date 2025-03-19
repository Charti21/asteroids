from circleshape import CircleShape
from constants import *
import pygame # type: ignore
import random

class Asteroid(CircleShape) :
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen) :
        pygame.draw.circle(screen,(255,255,255), self.position, self.radius, 2)
    
    def update(self, dt) :
        self.position += self.velocity * dt

    def split(self) :
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS :
            return
        #create a random number to be used for asteroid spawns
        random_angle = random.uniform(20,50)
        #Create two new velocity vectors by rotating by the random angle in both directions for the asteroid splits
        split_asteroid_vector1 = self.velocity.rotate(random_angle) * 1.2
        split_asteroid_vector2 = self.velocity.rotate(-random_angle) * 1.2
        #Create the new radius for asteroid splits
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        #Create the asteroids
        new_asteroid1= Asteroid(self.position.x,self.position.y, new_radius)
        new_asteroid1.velocity = split_asteroid_vector1 

        new_asteroid2=Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2.velocity = split_asteroid_vector2 
        

class Shot(CircleShape) :
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        
    def draw(self, screen) :
        pygame.draw.circle(screen, (255,255,255), self.position, SHOT_RADIUS) 
    
    def update(self,dt) :
        self.position += self.velocity * dt
        #print(f"Shot position updated to: {self.position}")  # Debugging
