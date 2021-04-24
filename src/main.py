import pygame, sys
from pygame.locals import *
from world import World
from entities.entity import Entity
from maps.tile import renderTile, TILE_TYPES, createTileData
from config import SCREEN_WIDTH, SCREEN_HEIGHT

world = World()
world.addEntity(Entity(world))

pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

while True: # main game loop

    # Clear the screen
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    world.update()
    world.render(DISPLAYSURF)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

