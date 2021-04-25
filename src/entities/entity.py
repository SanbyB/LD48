from resources import IMAGE_ENTITY
from physics import Physics
import pygame
import numpy as np
from config import SCREEN_WIDTH, SCREEN_HEIGHT
import random

class Entity(Physics):
    def __init__(self, x, y, width, height, world, hp):
        super().__init__(x, y, width, height)
        self.world = world
        self.hp = hp
        self.theta0, self.theta1 = None, None
        self.x_counter = 0
        self.y_counter = 0
        self.atk_counter = 0
        self.atk_speed = 50
        self.atk_strength = 2
        self.atk_range = 20000

    
    def update(self, camera, theta, strength):
        super().update()
        self.ray(camera)
        self.attacked(theta, strength, camera)
        self.attack(camera)
        self.move()
        self.death()

    def health_bar(self, screen, camera):
        if self.hp > 0:
            colour = (0, 255, 0)
            if self.hp < 10:
                colour = (240, 235, 86)
                if self.hp < 5:
                    colour = (240, 0 , 0)

            pygame.draw.rect(screen, colour, (self.x - camera.x, self.y - camera.y - (self.height * 0.6), self.hp*2, 5))


    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y
        scaledImage = pygame.transform.scale(IMAGE_ENTITY, (self.width, self.height)) 
        screen.blit(scaledImage, (xPos, yPos))
        self.health_bar(screen, camera)

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

    
    def attacked(self, theta, strength, camera):
        xPos = self.x - camera.x - SCREEN_WIDTH/2 + self.width/2
        yPos = self.y - camera.y - SCREEN_HEIGHT/2 + self.height/2

        if xPos**2 + yPos**2 < self.world.player.atk_range:

            if theta != None:  
                if self.theta0 > self.theta1:
                    if theta > self.theta0 or theta < self.theta1:
                        self.hp -= strength
                elif self.theta0 < theta < self.theta1:
                    self.hp -= strength



    def attack(self, camera):
        if self.world.player != None:
            xPos = self.x - camera.x - SCREEN_WIDTH/2 + self.width/2
            yPos = self.y - camera.y - SCREEN_HEIGHT/2 + self.height/2
            
            if xPos**2 + yPos**2 < self.atk_range:
                if self.atk_counter == 0:
                    self.world.player.hp -= self.atk_strength
                self.atk_counter += 1
                if self.atk_counter == self.atk_speed:
                    self.atk_counter = 0 


    
    def move(self):
        self.x_counter += 1
        self.y_counter += 1
        change_x_vel = 10000
        change_y_vel = 5000
        if self.x_counter == 300:
            self.x_counter = 0
        if self.y_counter == 150:
            self.y_counter = 0
        if self.x_counter > 100:
            change_x_vel = random.randint(100, 10000)
        if self.y_counter > 100:
            change_y_vel = random.randint(100, 5000)
        if self.x_counter > change_x_vel:
            self.x_vel = random.randrange(-4, 4)
            self.x_counter = 0
        if self.y_counter > change_y_vel:
            self.y_vel = -10

        self.x_vel = self.x_vel * 0.99
    

    def death(self):
        if self.hp <= 0:
            self.world.removeEntity(self)


