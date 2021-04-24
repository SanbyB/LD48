import pygame
from resources import IMAGE_PLAYER
from physics import Physics
from maps.tilemap import TILE_MAP_WIDTH, TILE_SIZE


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
        self.x_hit, self.y_hit = self.hit_box(IMAGE_PLAYER)
        self.invtry = []
        self.world = world
        self.didJump = False
        self.hp = 20

    def update(self):
        super().update()
        self.move()

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

