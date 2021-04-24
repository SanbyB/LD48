import pygame
import numpy as np
from resources import IMAGE_PLAYER
from physics import Physics
from maps.tilemap import TILE_MAP_WIDTH, TILE_SIZE
from config import SCREEN_WIDTH, SCREEN_HEIGHT


WALK_ACCN = 0.5
WALK_SPEED = 3
JUMP_POWER = 12

class Player(Physics):
    def __init__(self, world):
        super().__init__(
            (TILE_MAP_WIDTH / 2) * TILE_SIZE,
            -100,
            50,
            50
        )
        self.invtry = []
        self.world = world
        self.didJump = False
        self.hp = 20

    def update(self, camera):
        super().update()
        self.move()
        self.attack(camera)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.x_vel -= WALK_ACCN

        if keys[pygame.K_d]:
            self.x_vel += WALK_ACCN

        if self.x_vel > WALK_SPEED:
            self.x_vel = WALK_SPEED
        
        if self.x_vel < -WALK_SPEED:
            self.x_vel = -WALK_SPEED
    

        if keys[pygame.K_SPACE] and not self.didJump:
            self.didJump = True
            self.y_vel = -JUMP_POWER


    def render(self, screen, camera):
        xPos = self.x - camera.x
        yPos = self.y - camera.y
        scaledImage = pygame.transform.scale(IMAGE_PLAYER, (self.width, self.height)) 
        screen.blit(scaledImage, (xPos, yPos))
                
    def onHitFloor(self):
        super().onHitFloor()
        self.didJump = False

        # TODO dRemove this
        #self.world.tileMap.damageTile(self.x, self.y + self.height + 20, 0.1)


    def attack(self, camera):
        mouse = pygame.mouse.get_pressed()

        theta = -100

        if mouse[0] == 1:
            mp = pygame.mouse.get_pos()
            x_dist = SCREEN_WIDTH/2 - mp[0]
            y_dist = mp[1] - SCREEN_HEIGHT/2

            theta = np.angle(x_dist + y_dist * 1j) + np.pi

        return theta

