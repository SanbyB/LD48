import pygame

class Physics:
    def __init__(self, collision):
        self.x, self.y = 0, 0
        self.x_hit, self.y_hit = 0, 0 
        self.hp = 20
        self.grav = 0.05
        self.collision = collision

    def gravity(self):
        keys = pygame.key.get_pressed()

        if not self.collision:
            self.y_vel += self.grav

        else:
            if keys[pygame.K_SPACE]:
                self.y_vel = -5

            else:
                self.y_vel = 0
        
        self.y += self.y_vel

    
    def hit_box(self, name):
        im_size = name.get_width(), name.get_height()
        return im_size

        

