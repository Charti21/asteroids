import pygame # type: ignore
import random #for spawning asteroids
from asteroid import Asteroid 
from constants import *


class AsteroidField(pygame.sprite.Sprite):      #Spawns Asteroids on Edge of screen# Defining edges of spawns
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        self.spawn_timer += dt
        #print(f"Spawn timer: {self.spawn_timer}")  # Debug: Show timer incrementing
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0
            #print(f"Spawning asteroid...")  # Debug: Confirm spawning process starts

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            #print(f"Spawning asteroid of kind {kind} at {position} with velocity {velocity}")  # Debug info
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)