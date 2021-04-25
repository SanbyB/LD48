
from resources import SLIME_SHEET
from physics import Physics
import pygame
import numpy as np
from config import SCREEN_WIDTH, SCREEN_HEIGHT
import random
from animation import Animation

PARTICLE_SIZE = 8
DECAY = 0.01

class Particle(Physics):
    def __init__(self, world, x, y, colour):
        super().__init__(x, y, PARTICLE_SIZE, PARTICLE_SIZE)
        self.world = world
        self.colour = colour 
        self.life = 1.0  
        self.x_vel = random.uniform(-10, 10)
        self.y_vel = random.uniform(-10, 10)

    def update(self, camera):
        super().update()
        self.life -= DECAY
        if self.life < 0:
            self.world.removeEntity(self)
        self.width = PARTICLE_SIZE * self.life
        self.height = PARTICLE_SIZE * self.life


    def render(self, screen, camera):
        posX = self.x - camera.x
        posY = self.y - camera.y
        pygame.draw.rect(screen, self.colour, (posX, posY, self.width, self.height))

        
