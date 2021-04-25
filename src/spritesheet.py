
import pygame
from math import floor

class SpriteSheet:
    def __init__(self, image, xFrames, yFrames):
        self.image = image
        self.xFrames = xFrames
        self.yFrames = yFrames
        self.ImageWidth = self.image.get_width() / self.xFrames
        self.ImageHeight = self.image.get_height() / self.yFrames

    def draw(self, surface, xFrame, yFrame, x, y, width, height, direction, angle = 10):
        xUpscale = width / self.ImageWidth
        yUpscale = height / self.ImageHeight
        scaledImage = pygame.transform.scale(self.image, (floor(xUpscale * self.xFrames * self.ImageWidth), floor(yUpscale * self.yFrames * self.ImageHeight))) 
        flippedImage = pygame.transform.flip(scaledImage, True, False) if direction else scaledImage
        surface.blit(flippedImage, (x, y), (xFrame * width, yFrame * height, width, height))

