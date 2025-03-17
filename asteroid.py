from circleshape import CircleShape
from constants import *
import pygame # type: ignore

class Asteroid(CircleShape) :
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
    def draw(self, screen) :
        pygame.draw.circle(screen,(255,255,255), self.position, self.radius, 2)
    
    def update(self, dt) :
        self.position += self.velocity * dt

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
