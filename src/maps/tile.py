import pygame
from pygame import Rect
from resources import TILE_ROCK_00

class Tile:
    def __init__(self, type, tileX, tileY):
        self.type = type
        return

    def render(self, surface, x, y, size, tiles):
        return

class Rock(Tile):
    def __init__(self, tileX, tileY):
        super().__init__("ROCK", tileX, tileY)
    
    def render(self, surface, x, y, size, tiles):
        scaledImage = pygame.transform.scale(TILE_ROCK_00, (size, size)) 
        surface.blit(scaledImage, (x, y))
        return

class Air(Tile):
    def __init__(self, tileX, tileY):
        super().__init__("Air", tileX, tileY)

    def render(self, surface, x, y, size, tiles):
        return
