import pygame
from pygame import Rect

TILE_TYPES = {
    "ROCK": 0
}

# Create the tile data to store in the tile array
# type - integer of the tile type
def createTileData(type): 
    return {
        "TYPE": type,
        "HEALTH": 1.0
    }

# Render a tile based on its data
# tileData - info about the tile (is it Rock etc)
# x - the x position on screen px
# y - the y position on screen px
# size - the size of the tile px
def renderTile(surface, tileData, x, y, size): 
    pygame.draw.rect(surface, (255, 0, 0), Rect(x, y, size, size))
    pygame.draw.rect(surface, (255, 255, 255), Rect(x, y, size, size), 3)

    