import os.path
import pygame
from spritesheet import SpriteSheet
from animation import Animation

pygame.init()


IMAGE_PLAYER = pygame.image.load(os.path.join("Graphics", "Player.png"))

FONT = 0
FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 72)
SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 36)


ORE_SHEET = SpriteSheet(pygame.image.load(os.path.join("Graphics", "ore.png")), 1, 1)
PLAYER_SHEET = SpriteSheet(pygame.image.load(os.path.join("Graphics", "miner.png")), 8, 5)
PLAYER_BREATHING = Animation(PLAYER_SHEET, 0, 0.1)
PLAYER_WALKING = Animation(PLAYER_SHEET, 1, 0.2)
PLAYER_JUMPING = Animation(PLAYER_SHEET, 2, 0.2)
PLAYER_FALLING = Animation(PLAYER_SHEET, 3, 0.2)
PLAYER_HURT = Animation(PLAYER_SHEET, 4, 0.2)

EQUIPMENT_PICKAXE = pygame.image.load(os.path.join("Graphics", "equipment.png"))

SLIME_SHEET = SpriteSheet(pygame.image.load(os.path.join("Graphics", "slime.png")), 8, 4)

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


