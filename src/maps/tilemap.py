

from maps.tile import renderTile, createTileData, TILE_TYPES
from math import ceil

TILE_MAP_WIDTH = 20
TILE_SIZE = 30

class TileMap:
    def __init__(self, onGenerateListener):
        self.tiles = []
        self.onGenerateListener = onGenerateListener
        self.generateRow()
        return

    def render(self, surface, camera):
        # TODO insert camera position here
        xPos = 0
        yPos = 0
        xWidth = 640
        yWidth = 480

        # When camera is lower than what we've generated, generate more tiles
        targetTileHeight = ceil((yPos + yWidth) / TILE_SIZE)
        if (targetTileHeight > len(self.tiles)):
            for x in range(targetTileHeight - len(self.tiles)):
                self.generateRow()

        # Draw the tiles
        # TODO we should only render tiles on screen
        for tileY in range(len(self.tiles)):
            for tileX in range(TILE_MAP_WIDTH):
                xRender = (tileX * TILE_SIZE)
                yRender = (tileY * TILE_SIZE) 
                tile = self.tiles[tileY][tileX]
                renderTile(surface, tile, xRender, yRender, TILE_SIZE)
        return

    
    def generateRow(self):
        y = len(self.tiles)
        newRow = []
        for x in range(TILE_MAP_WIDTH):
            newRow.append(self.generateTile(x, y))
        self.tiles.append(newRow)
        self.onGenerateListener(y)

    def generateTile(self, x, y):
        return createTileData(TILE_TYPES["ROCK"])
        









