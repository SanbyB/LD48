import pygame
import numpy as np
from resources import PLAYER_BREATHING, PLAYER_WALKING, PLAYER_JUMPING, PLAYER_FALLING, PLAYER_HURT
from physics import Physics
from maps.tilemap import TILE_MAP_WIDTH, TILE_SIZE
from config import SCREEN_WIDTH, SCREEN_HEIGHT


WALK_ACCN = 1.5
WALK_SPEED = 5
JUMP_POWER = 12

class Player(Physics):
    def __init__(self, world):
        super().__init__(
            (TILE_MAP_WIDTH / 2) * TILE_SIZE,
            -100,
            40,
            64
        )
        self.invtry = []
        self.world = world
        self.didJump = False
        self.hp = 20
        self.theta = None  # angle of attack
        self.atk_counter = 0
        self.atk_speed = 50
        self.atk_strength = 3
        self.atk_range = 30000
        self.isFlipped = False
        self.hitCount = 0

    def update(self):
        super().update()
        self.move()
        self.attack()
        self.fall_damage()

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

        self.x_vel = self.x_vel * 0.8


    def health_bar(self, screen):
        if self.hp > 0:
            colour = (0, 255, 0)
            if self.hp < 10:
                colour = (240, 235, 86)
                if self.hp < 5:
                    colour = (240, 0 , 0)

            pygame.draw.rect(screen, colour, (SCREEN_WIDTH/2 - 20, SCREEN_HEIGHT/2 - (self.height * 0.6), self.hp*2, 5))




    def render(self, screen, camera):
        imageInflate = 12
        xPos = self.x - camera.x - imageInflate
        yPos = self.y - camera.y

        isFalling = self.y_vel > 0.05
        isJumping = self.y_vel < -0.05
        isWalking = abs(self.x_vel) > 0.05 and not (isFalling or isJumping)

        if self.x_vel < 0:
            self.isFlipped = True

        if self.x_vel > 0:
            self.isFlipped = False

        width = self.width + imageInflate * 2

        if self.hitCount > 0:
            self.hitCount -= 1
            PLAYER_HURT.update()
            PLAYER_HURT.draw(screen, xPos, yPos, width, self.height, self.isFlipped)
        elif isWalking:
            PLAYER_WALKING.update()
            PLAYER_WALKING.draw(screen, xPos, yPos, width, self.height, self.isFlipped)
        elif isFalling:
            PLAYER_FALLING.update()
            PLAYER_FALLING.draw(screen, xPos, yPos, width, self.height, self.isFlipped)
        elif isJumping:
            PLAYER_JUMPING.update()
            PLAYER_JUMPING.draw(screen, xPos, yPos, width, self.height, self.isFlipped)
        else: 
            PLAYER_BREATHING.update()
            PLAYER_BREATHING.draw(screen, xPos, yPos, width, self.height, self.isFlipped)

        self.health_bar(screen)

      
                
    def onHitFloor(self):
        super().onHitFloor()
        self.didJump = False


    def onHitByEntity(self, amount, x, y):
        self.hp -= amount
        diffX = self.x - x
        HIT_AMOUNT = 40
        self.x_vel += HIT_AMOUNT if diffX > 0 else -HIT_AMOUNT
        self.hitCount = 10
        PLAYER_HURT.reset()


    def fall_damage(self):
        if self.y_vel > 7.5:
            self.hp -= 1


    def attack(self):
        mouse = pygame.mouse.get_pressed()
        
        self.theta = None
        distance = TILE_SIZE * 0.9

        if mouse[0] == 1:
            mp = pygame.mouse.get_pos()
            x_dist = SCREEN_WIDTH/2 - mp[0]
            y_dist = mp[1] - SCREEN_HEIGHT/2

            theta = np.angle(x_dist + y_dist * 1j) + np.pi

            targetX = (distance * np.cos(theta)) + self.x + self.width / 2
            targetY = -distance * np.sin(theta) + self.y + self.height / 2
            self.world.tileMap.damageTile(targetX, targetY, 0.1)

            if self.atk_counter == 0:
                self.theta = theta

            self.atk_counter += 1

        elif self.atk_counter != 0:
            self.atk_counter += 1

        if self.atk_counter == self.atk_speed:
            self.atk_counter = 0

    
                
                

        





        


