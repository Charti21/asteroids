from circleshape import CircleShape
from constants import *
from asteroid import Shot

import pygame # type: ignore

class Player(CircleShape) :
    def __init__(self,x,y) :
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
    

    def triangle(self):    #Creating triangular picture on screen, although hitbox is going to be circular.
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
        if keys[pygame.K_a]:      #If a is pressed rotate in a negative (counter-clockwise)direction
            self.rotate(-dt)
        if keys[pygame.K_d]:      # If d is pressed rotate in a positive (clockwise) direction
            self.rotate(dt)
        if keys[pygame.K_w]:      #if w is pressed move forward
            self.move(dt)
        if keys[pygame.K_s]:      #if s is pressed move backward
            self.move(-dt)
        if keys[pygame.K_SPACE] :   #if space bar is pressed call the shoot method provided in asteroid.py file, which should create bullets spawning from player. 
            if self.timer <= 0 :    #The amount of shots fired per second is limited by the constant provided as player_shoot_cooldown
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
        
       
        