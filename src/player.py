import pygame
from resources import IMAGE_PLAYER
from physics import Physics


class Player(Physics):
    def __init__(self, collision):
        super().__init__(collision)
        self.invtry = []
        self.x_vel = 2
        self.x_hit, self.y_hit = self.hit_box(IMAGE_PLAYER)


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

        
    def render(self, screen):
        screen.blit(IMAGE_PLAYER, (self.x, self.y))
                

