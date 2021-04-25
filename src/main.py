import pygame, sys
from pygame.locals import *
from world import World
from player import Player
from camera import Camera
from entities.entity import Entity
from config import SCREEN_WIDTH, SCREEN_HEIGHT

world = World()
world.addEntity(Entity(4000, -100, 50, 50, world, 20))
player = Player(world)
world.player = player
cam = Camera()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

clock = pygame.time.Clock()

while True: # main game loop
    dt = clock.tick(10)
    # Clear the screen
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    player.update()
    cam.move(player)
    player.render(DISPLAYSURF, cam)
    world.update(cam)
    world.render(DISPLAYSURF, cam)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()

