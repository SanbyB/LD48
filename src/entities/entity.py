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
        self.theta0, self.theta1 = None, None
        self.hit = False

    
    def update(self, camera, theta):
        super().update()
        self.ray(camera)
        self.attacked(theta)
        self.death()


    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y
        scaledImage = pygame.transform.scale(IMAGE_ENTITY, (self.width, self.height)) 
        screen.blit(scaledImage, (xPos, yPos))

    def ray(self, camera):
        # Targeting the entity

        xPos = self.x - camera.x - SCREEN_WIDTH/2 + self.width/2
        yPos = -(self.y - camera.y) + SCREEN_HEIGHT/2 - self.width/2

        '''
        The positive, positive quadrant and the negative, negative quadrant 
        both use the top left and bottom right corners of the hit box,
        where as the negative positive and vise versa
        use the top right and bottom left corners of the hit box
        '''
        x0, y0, x1, y1 = 0, 0, 0, 0

        
        if yPos >= 0:
            x0 = xPos + self.width/2
            x1 = xPos - self.width/2
        else:
            x0 = xPos - self.width/2
            x1 = xPos + self.width/2

        if xPos >= 0:
            y0 = yPos - self.height/2
            y1 = yPos + self.height/2
        else:
            y0 = yPos + self.height/2
            y1 = yPos - self.height/2

        
        self.theta0 = np.angle(-x0 - y0 * 1j) + np.pi
        self.theta1 = np.angle(-x1 - y1 * 1j) + np.pi

    
    def attacked(self, theta):
        self.hit = False

        if theta != None:

            if self.theta0 > self.theta1:
                if theta > self.theta0 or theta < self.theta1:
                    self.hit = True
            elif self.theta0 < theta < self.theta1:
                self.hit = True


    def death(self):
        if self.hp <= 0:
            self.world.removeEntity(self)


