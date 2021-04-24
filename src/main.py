import pygame, sys
from pygame.locals import *
from world import World
from entities.entity import Entity

world = World()
world.addEntity(Entity(world))

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: # main game loop
    world.update()
    world.render()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    