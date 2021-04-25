import pygame, sys
from pygame.locals import *
from world import World
from player import Player
from camera import Camera
from entities.entity import Entity
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from inventory import Inventory
from resources import FONT
from ui import UI


cam = Camera()
world = World(cam)
ui = UI(world)
world.addEntity(Entity(4000, -100, 50, 50, world, 20))
player = Player(world)
world.player = player
inventory = Inventory()
inventory.player = player

pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

clock = pygame.time.Clock()

while True: # main game loop
    dt = clock.tick(60)
    # Clear the screen
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    player.update()
    cam.move(player)
    inventory.update()
    player.render(DISPLAYSURF, cam)
    world.update(cam)
    world.render(DISPLAYSURF, cam)
    ui.draw(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
