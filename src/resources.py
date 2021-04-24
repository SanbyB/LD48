import os.path
import pygame
from spritesheet import SpriteSheet

IMAGE_PLAYER = pygame.image.load(os.path.join("Graphics", "Player.png"))

IMAGE_ENTITY = pygame.image.load(os.path.join("Graphics", "Entity.png"))

TILE_BREAKING = SpriteSheet(pygame.image.load(os.path.join("Graphics", "breaking.png")), 5, 1)
TILE_ROCK_00 = pygame.image.load(os.path.join("Graphics", "tiles", "Tile_12.png"))



