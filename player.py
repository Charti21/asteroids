from circleshape import CircleShape
from constants import *
from asteroid import Shot

import pygame # type: ignore

class Player(CircleShape) :
    def __init__(self,x,y) :
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    # in the player class

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen) :
        pygame.draw.polygon(screen,(255,255,255),self.triangle(),2)

    def rotate(self, dt) :
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] :
            if self.timer <= 0 :
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN
                
            
                
            


    def move(self, dt) :
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self) :
        Shot(self.position.x, self.position.y, self.rotation)  # Attempt shot creation
        

        #Debugging help
        #print(f"Player shooting from position: {self.position} with rotation: {self.rotation}")
        #try:
        #    Shot(self.position.x, self.position.y, self.rotation)  # Attempt shot creation
        #except Exception as e:
        #    print(f"Error while creating Shot: {e}")  # Catch and log any issue
        
       
        