import pygame
from resources import IMAGE_PLAYER

class Player:
    def __init__(self, collision):
        self.x, self.y = 0, 0
        self.x_vel = 2
        self.y_vel = 1
        self.hp = 10
        self.invtry = []
        self.collision = collision


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.x_vel

        if keys[pygame.K_d]:
            self.x += self.x_vel

        if keys[pygame.K_w]:
            self.y -= self.x_vel

        if keys[pygame.K_s]:
            self.y += self.x_vel


    def gravity(self, collision):
        keys = pygame.key.get_pressed()

        if not collision:
            grav_accn = 0.05
            self.y_vel += grav_accn

        else:
            if keys[pygame.K_SPACE]:
                self.y_vel = -5

            else:
                self.y_vel = 0
        
        self.y += self.y_vel

        


    def render(self, screen):
        screen.blit(IMAGE_PLAYER, (self.x, self.y))
                

