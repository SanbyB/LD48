from resources import IMAGE_ENTITY
from physics import Physics
import pygame
import numpy as np
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Entity(Physics):
    def __init__(self, x, y, width, height, world, hp):
        super().__init__(x, y, width, height)
        self.world = world
        self.hp = hp

    
    def update(self):
        super().update()
        self.death()


    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y
        scaledImage = pygame.transform.scale(IMAGE_ENTITY, (self.width, self.height)) 
        screen.blit(scaledImage, (xPos, yPos))

    def ray(self, camera):
        # Targeting the entity

        xPos = self.x - camera.x - SCREEN_WIDTH/2
        yPos = -(self.y - camera.y) + SCREEN_HEIGHT/2

        '''
        The positive, positive quadrant and the negative, negative quadrant 
        both use the top left and bottom right corners of the hit box,
        where as the negative positive and vise versa
        use the top right and bottom left corners of the hit box
        '''

        x0, y0 = xPos + self.width/2, yPos + self.height/2
        x1, y1 = xPos - self.width/2, yPos - self.height/2

        if (xPos > 0 and yPos > 0) or (xPos < 0 and yPos < 0): 
            x0, y0 = xPos + self.width/2, yPos - self.height/2
            x1, y1 = xPos - self.width/2, yPos + self.height/2

        theta0 = np.angle(-x0 - y0 * 1j) + np.pi
        theta1 = np.angle(-x1 - y1 * 1j) + np.pi

        return theta0, theta1


    def death(self):
        if self.hp <= 0:
            self.world.removeEntity(self)


