import pygame, sys
from pygame.locals import *
from world import World
from player import Player
from camera import Camera
from entities.entity import Entity
from config import SCREEN_WIDTH, SCREEN_HEIGHT

world = World()
world.addEntity(Entity(world))
player = Player(world)
cam = Camera()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

while True: # main game loop

    # Clear the screen
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    player.update()
    cam.move(player)
    player.render(DISPLAYSURF, cam)
    world.update()
    world.render(DISPLAYSURF, cam)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()

