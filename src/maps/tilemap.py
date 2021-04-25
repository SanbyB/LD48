

from maps.tile import Rock, Air, Ore
from math import ceil, floor
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from entities.entity import Entity
import random
import pygame

TILE_MAP_WIDTH = 20
TILE_SIZE = 80

class TileMap:
    def __init__(self, world, onGenerateListener):
        self.world = world
        self.tiles = []
        self.onGenerateListener = onGenerateListener
        self.generateChunk()
        return

    def render(self, surface, camera):
        xPos = camera.x
        yPos = camera.y
        xWidth = SCREEN_WIDTH
        yHeight = SCREEN_HEIGHT

        # When camera is lower than what we've generated, generate more tiles
        targetTileHeight = ceil((yPos + yHeight) / TILE_SIZE) + 10
        if (targetTileHeight > len(self.tiles)):
            for x in range(targetTileHeight - len(self.tiles)):
                self.generateChunk()

        xTilePos = floor(xPos / TILE_SIZE)
        yTilePos = floor(yPos / TILE_SIZE)
        xTileWidth = ceil((xPos + xWidth) / TILE_SIZE)
        yTileHeight = ceil((yPos + yHeight) / TILE_SIZE)

        xTilePos = min(max(xTilePos, 0), TILE_MAP_WIDTH)
        yTilePos = min(max(yTilePos, 0), len(self.tiles))
        xTileWidth = min(max(xTileWidth, 0), TILE_MAP_WIDTH)
        yTileHeight = min(max(yTileHeight, 0), len(self.tiles))

        # Draw the tiles
        for tileY in range(yTilePos, yTileHeight):
            for tileX in range(xTilePos, xTileWidth):
                xRender = (tileX * TILE_SIZE) - xPos
                yRender = (tileY * TILE_SIZE) - yPos
                tile = self.tiles[tileY][tileX]
                tile.render(surface, xRender, yRender, TILE_SIZE, self.tiles)

        
        return
    
    def generateChunk(self):
        for i in range(0, 5):
            self.generateRow()

        y = len(self.tiles)
        bottomRock = []
        for x in range(TILE_MAP_WIDTH):
            bottomRock.append(Rock(self.world, x, y))
        self.tiles.append(bottomRock)
        self.onGenerateListener(y)

    def generateRow(self):
        y = len(self.tiles)
        newRow = []
        for x in range(TILE_MAP_WIDTH):
            newRow.append(self.generateTile(x, y))
        self.tiles.append(newRow)
        self.onGenerateListener(y)

    def generateTile(self, x, y):
        value = random.uniform(0, 1)
        if value > 0.95:
            tile = Ore(self.world, x, y)
        elif value > 0.5:
            tile = Rock(self.world, x, y)
        else:
            tile = Air(self.world, x, y)
            if value < 0.05:
                xPos = x * TILE_SIZE + TILE_SIZE / 2 - 25
                yPos = y * TILE_SIZE + TILE_SIZE / 2 - 25
                self.world.addEntity(Entity(xPos, yPos, 50, 50, self.world, 20))
        
        return tile

    def doesCollide(self, x, y):
        xTilePos = floor(x / TILE_SIZE)
        yTilePos = floor(y / TILE_SIZE)
        if (xTilePos < 0 or xTilePos >= TILE_MAP_WIDTH):
            return True
        if (yTilePos < 0 or yTilePos >= len(self.tiles)):
            return False
        return self.tiles[yTilePos][xTilePos].doesCollide

    def damageTile(self, x, y, amount):
        xTilePos = floor(x / TILE_SIZE)
        yTilePos = floor(y / TILE_SIZE)
        if (xTilePos < 0 or xTilePos >= TILE_MAP_WIDTH):
            return
        if (yTilePos < 0 or yTilePos >= len(self.tiles)):
            return
        self.tiles[yTilePos][xTilePos].onDamage(amount)

    def replaceTile(self, x, y, tile):
        if (x < 0 or x >= TILE_MAP_WIDTH):
            return
        if (y < 0 or y >= len(self.tiles)):
            return
        self.tiles[y][x] = tile
        









