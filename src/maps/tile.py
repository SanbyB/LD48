import pygame
from pygame import Rect
from resources import TILE_ROCK_00, TILE_BREAKING
import random
from math import ceil, floor

class Tile:
    def __init__(self, world, type, tileX, tileY, doesCollide):
        self.world = world
        self.type = type
        self.doesCollide = doesCollide
        self.tileX = tileX
        self.tileY = tileY
        return

    def render(self, surface, x, y, size, tiles):
        return

    def onDamage(self, amount):
        return

class Rock(Tile):
    def __init__(self, world, tileX, tileY):
        super().__init__(world, "ROCK", tileX, tileY, True)
        self.health = random.uniform(0, 1.0)
    
    def render(self, surface, x, y, size, tiles):
        scaledImage = pygame.transform.scale(TILE_ROCK_00, (size, size)) 
        surface.blit(scaledImage, (x, y))
        tileHealth = 5 - ceil(self.health * 5)
        TILE_BREAKING.draw(surface, tileHealth, 0, x, y, size, size)
        return

    def onDamage(self, amount):
        self.health -= amount
        if (self.health < 0):
            self.health = 0
            self.world.tileMap.replaceTile(self.tileX, self.tileY, Air(self.world, self.tileX, self.tileX))
        return

class Air(Tile):
    def __init__(self, world, tileX, tileY):
        super().__init__(world, "Air", tileX, tileY, False)

    def render(self, surface, x, y, size, tiles):
        return
