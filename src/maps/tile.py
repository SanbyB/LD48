import pygame
from pygame import Rect
from resources import TILE_ROCK, TILE_BREAKING
import random
from math import ceil, floor

def getCode(tiles, x, y):
    top = "_"
    if y > 0 and tiles[y - 1][x].doesCollide:
        top = "B"
    bottom = "_"
    if y < len(tiles) - 1 and tiles[y + 1][x].doesCollide:
        bottom = "B"
    left = "_"
    if x > 0 and tiles[y][x - 1].doesCollide:
        left = "B"
    right = "_"
    if x < len(tiles[y]) - 1 and tiles[y][x + 1].doesCollide:
        right = "B"

    return top + right + bottom + left

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

        image = TILE_ROCK[getCode(tiles, self.tileX, self.tileY)]

        scaledImage = pygame.transform.scale(image, (size, size)) 


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
