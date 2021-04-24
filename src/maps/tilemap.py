

from maps.tile import Rock, Air
from math import ceil
from config import SCREEN_WIDTH, SCREEN_HEIGHT
import random

TILE_MAP_WIDTH = 20
TILE_SIZE = 30

class TileMap:
    def __init__(self, onGenerateListener):
        self.tiles = []
        self.onGenerateListener = onGenerateListener
        self.generateRow()
        return

    def render(self, surface, camera):
        xPos = camera.x
        yPos = camera.y
        xWidth = SCREEN_WIDTH
        yHeight = SCREEN_HEIGHT

        # When camera is lower than what we've generated, generate more tiles
        targetTileHeight = ceil((yPos + yHeight) / TILE_SIZE)
        if (targetTileHeight > len(self.tiles)):
            for x in range(targetTileHeight - len(self.tiles)):
                self.generateRow()

        # Draw the tiles
        # TODO we should only render tiles on screen
        for tileY in range(len(self.tiles)):
            for tileX in range(TILE_MAP_WIDTH):
                xRender = (tileX * TILE_SIZE) - xPos
                yRender = (tileY * TILE_SIZE) - yPos
                tile = self.tiles[tileY][tileX]
                tile.render(surface, xRender, yRender, TILE_SIZE, self.tiles)
        return

    
    def generateRow(self):
        y = len(self.tiles)
        newRow = []
        for x in range(TILE_MAP_WIDTH):
            newRow.append(self.generateTile(x, y))
        self.tiles.append(newRow)
        self.onGenerateListener(y)

    def generateTile(self, x, y):
        value = random.uniform(0, 1)
        tile = Rock(x, y) if value > 0.5 else Air(x, y)
        return tile

        









