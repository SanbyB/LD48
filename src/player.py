import pygame
from resources import IMAGE_PLAYER

class Player:
    def __init__(self):
        self.x, self.y = 0, 0
        self.vel = 10
        self.hp = 10
        self.invtry = []


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x -= self.vel

        if keys[pygame.K_d]:
            self.x += self.vel

        if keys[pygame.K_w]:
            self.y -= self.vel

        if keys[pygame.K_s]:
            self.y += self.vel


    def render(self, screen):
        screen.blit(IMAGE_PLAYER, (self.x, self.y))
                

