import pygame
from pygame import Rect
from resources import TILE_ROCK, TILE_BREAKING, ORE_SHEET, audio
import random
from math import ceil, floor
from particle import Particle

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
        TILE_BREAKING.draw(surface, tileHealth, 0, x, y, size, size, False)
        return

    def onDamage(self, amount):
        self.health -= amount
        self.world.camera.shake(4)
        if (self.health < 0):
            audio.onRockBreak()
            self.health = 0
            self.world.tileMap.replaceTile(self.tileX, self.tileY, Air(self.world, self.tileX, self.tileX))
            for i in range(0, 10):
                posX = random.uniform(self.tileX * 80, (self.tileX + 1) * 80)
                posY = random.uniform(self.tileY * 80, (self.tileY + 1) * 80)
                particle = Particle(self.world, posX, posY, (115, 62, 57))
                self.world.addEntity(particle)
        else:
            audio.onRockHit()
        return

class Ore(Tile):
    def __init__(self, world, tileX, tileY):
        super().__init__(world, "ORE", tileX, tileY, True)
        self.health = random.uniform(0, 1.0)
    
    def render(self, surface, x, y, size, tiles):
        image = TILE_ROCK[getCode(tiles, self.tileX, self.tileY)]
        scaledImage = pygame.transform.scale(image, (size, size)) 
        surface.blit(scaledImage, (x, y))
        ORE_SHEET.draw(surface, 0, 0, x, y, size, size, False)
        tileHealth = 5 - ceil(self.health * 5)
        TILE_BREAKING.draw(surface, tileHealth, 0, x, y, size, size, False)
        return

    def onDamage(self, amount):
        self.health -= amount
        self.world.camera.shake(4)
        if (self.health < 0):
            audio.onOreBreak()
            self.health = 0
            self.world.tileMap.replaceTile(self.tileX, self.tileY, Air(self.world, self.tileX, self.tileX))
            for i in range(0, 10):
                posX = random.uniform(self.tileX * 80, (self.tileX + 1) * 80)
                posY = random.uniform(self.tileY * 80, (self.tileY + 1) * 80)
                particle = Particle(self.world, posX, posY, (115, 62, 57))
                self.world.addEntity(particle)
            for i in range(0, 10):
                posX = random.uniform(self.tileX * 80, (self.tileX + 1) * 80)
                posY = random.uniform(self.tileY * 80, (self.tileY + 1) * 80)
                particle = Particle(self.world, posX, posY, (192, 203, 220))
                self.world.addEntity(particle)
            self.world.player.onOrePickup()
        else:
            audio.onOreHit()
        return


class Air(Tile):
    def __init__(self, world, tileX, tileY):
        super().__init__(world, "Air", tileX, tileY, False)

    def render(self, surface, x, y, size, tiles):
        return
