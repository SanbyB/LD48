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
from maps.tilemap import TILE_MAP_WIDTH, TILE_SIZE


class Game:
    def __init__(self):
        self.hasStarted = False
        self.hasDied = False
        self.highScore = 0
        self.reset()

    def reset(self):
        self.cam = Camera()  
        self.world = World(self.cam)
        self.ui = UI(self.world)
        self.player = Player(self.world, self.onPlayerDead)
        self.world.player = self.player
        self.inventory = Inventory()
        self.inventory.player = self.player

    def update(self):

        keys = pygame.key.get_pressed()
        if not self.hasStarted:
            if keys[pygame.K_RETURN]:
                self.hasStarted = True

        if self.hasDied:
            if keys[pygame.K_RETURN]:
                self.reset()
                self.hasDied = False

        if self.hasDied or not self.hasStarted:
            return
        self.player.update()
        self.cam.move(game.player)
        self.inventory.update()
        self.world.update(game.cam)
        


    def render(self, DISPLAYSURF):
        self.world.render(DISPLAYSURF, game.cam)
        if not self.hasStarted:
            self.ui.renderStartingScreen(DISPLAYSURF)
        elif self.hasDied:
            self.ui.renderDiedScreen(DISPLAYSURF, self.highScore)
        else:
            self.ui.draw(DISPLAYSURF)

    def onPlayerDead(self):
        self.hasDied = True
        self.highScore = max(self.player.score, self.highScore)


game = Game()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello World!')

clock = pygame.time.Clock()

while True: # main game loop
    dt = clock.tick(60)
    # Clear the screen
    pygame.draw.rect(DISPLAYSURF, (0, 0, 0, 255), Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))

    game.update()
    game.render(DISPLAYSURF)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    
    pygame.display.update()
