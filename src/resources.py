import os.path
import pygame
from spritesheet import SpriteSheet

IMAGE_PLAYER = pygame.image.load(os.path.join("Graphics", "Player.png"))

IMAGE_ENTITY = pygame.image.load(os.path.join("Graphics", "Entity.png"))

TILE_BREAKING = SpriteSheet(pygame.image.load(os.path.join("Graphics", "breaking.png")), 5, 1)


TILE_ROCK_00 = pygame.image.load(os.path.join("Graphics", "tiles", "Tile_12.png"))

# 0 - TOP, 1 - RIGHT, 2 - BOTTOM, 3 - LEFT
TILE_ROCK = {
    "BBBB": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_12.png")),
    "BBB_": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_11.png")),
    "BB_B": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_22.png")),
    "BB__": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_21.png")),
    "B_BB": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_14.png")),
    "B_B_": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_55.png")),
    "B__B": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_23.png")),
    "B___": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_56.png")),
    "_BBB": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_25.png")),
    "_BB_": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_01.png")),
    "_B_B": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_33.png")),
    "_B__": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_32.png")),
    "__BB": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_03.png")),
    "__B_": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_54.png")),
    "___B": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_34.png")),
    "____": pygame.image.load(os.path.join("Graphics", "tiles", "Tile_31.png"))
}


