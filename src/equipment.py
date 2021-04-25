from resources import EQUIPMENT_PICKAXE
import pygame
from math import floor, cos, sin

EQUIPMENT_SIZE = 40
HAND_LENGTH = 20
HAND_ANGLE = 45
SWING = 180
class Equipment:
    def __init__(self, world, player):
        self.world = world
        self.player = player
        self.x = player.x
        self.y = player.y 
        self.targetX = player.x
        self.targetY = player.y
        self.angle = HAND_ANGLE
        self.targetAngle = HAND_ANGLE
        self.swing = 0

    def update(self):
        flipAdd = HAND_LENGTH if self.player.isFlipped else -HAND_LENGTH

        self.targetX = self.player.x + (self.player.width / 2) - (EQUIPMENT_SIZE / 2) 
        self.targetY = self.player.y + (self.player.height / 2) - (EQUIPMENT_SIZE / 2)
        ang = -HAND_ANGLE + self.swing
        self.targetAngle = (ang if self.player.isFlipped else -ang)
        self.swing = self.swing * 0.8
        if self.swing < 0.1:
            self.swing = 0

        self.x = self.x + (self.targetX - self.x) * 0.5
        self.y = self.y + (self.targetY - self.y) * 0.5
        self.angle = self.angle + (self.targetAngle - self.angle) * 0.5


        return

    def render(self, surface, camera):

        radians = (self.angle / 180) * 3.1415

        posX = self.x - camera.x - floor(HAND_LENGTH * sin(radians))
        posY = self.y - camera.y - floor(HAND_LENGTH * cos(radians))
        direction = True
        scaledImage = pygame.transform.scale(EQUIPMENT_PICKAXE, (EQUIPMENT_SIZE, EQUIPMENT_SIZE)) 
        flippedImage = pygame.transform.flip(scaledImage, True, False) if direction else scaledImage
        rotatedImage = pygame.transform.rotate(flippedImage, self.angle)
        surface.blit(rotatedImage, (posX, posY))
        return


    def onAttack(self):
        if self.swing > 0:
            return
        self.swing = SWING
        return


