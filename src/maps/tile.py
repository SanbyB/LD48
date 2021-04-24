import pygame
from pygame import Rect
from resources import TILE_ROCK_00

class Tile:
    def __init__(self, world, type, tileX, tileY, doesCollide):
        self.world = world
        self.type = type
        self.doesCollide = doesCollide
        return

    def render(self, surface, x, y, size, tiles):
        return

class Rock(Tile):
    def __init__(self, world, tileX, tileY):
        super().__init__(world, "ROCK", tileX, tileY, True)
    
    def render(self, surface, x, y, size, tiles):
        scaledImage = pygame.transform.scale(TILE_ROCK_00, (size, size)) 
        surface.blit(scaledImage, (x, y))
        return

class Air(Tile):
    def __init__(self, world, tileX, tileY):
        super().__init__(world, "Air", tileX, tileY, False)

    def render(self, surface, x, y, size, tiles):
        return
