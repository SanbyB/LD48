import os.path
import pygame
from spritesheet import SpriteSheet
from animation import Animation

pygame.init()


IMAGE_PLAYER = pygame.image.load(os.path.join("Graphics", "Player.png"))

FONT = 0
FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 72)
SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 36)
EVEN_SMALLER_FONT = pygame.font.Font(os.path.join("Graphics", "ARCADECLASSIC.TTF"), 28)


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


BACKGROUND_VOLUME = 0.02
MAIN_VOLUME = 0.04

SOUND_BIP = pygame.mixer.Sound(os.path.join("Audio", "bip.mp3"))
SOUND_BIP.set_volume(MAIN_VOLUME)

SOUND_SMOT = pygame.mixer.Sound(os.path.join("Audio", "smot.mp3"))
SOUND_SMOT.set_volume(MAIN_VOLUME)

SOUND_FOOTSTEP = pygame.mixer.Sound(os.path.join("Audio", "footstep.mp3"))
SOUND_FOOTSTEP.set_volume(MAIN_VOLUME)

SOUND_HIT = pygame.mixer.Sound(os.path.join("Audio", "bleurf.mp3"))
SOUND_HIT.set_volume(MAIN_VOLUME)

SOUND_HIT2 = pygame.mixer.Sound(os.path.join("Audio", "hit.mp3"))
SOUND_HIT2.set_volume(MAIN_VOLUME)

SOUND_HIT3 = pygame.mixer.Sound(os.path.join("Audio", "hit2.mp3"))
SOUND_HIT3.set_volume(MAIN_VOLUME)

SOUND_HIT4 = pygame.mixer.Sound(os.path.join("Audio", "hit3.mp3"))
SOUND_HIT4.set_volume(MAIN_VOLUME)

SOUND_POINT = pygame.mixer.Sound(os.path.join("Audio", "point.mp3"))
SOUND_POINT.set_volume(MAIN_VOLUME)


class Audio():
    def playMusic(self):
        pygame.mixer.music.load(os.path.join("Audio", "background.mp3")) 
        pygame.mixer.music.set_volume(BACKGROUND_VOLUME)     
        pygame.mixer.music.play(-1,0.0)  

    def onRockHit(self):
        SOUND_SMOT.play()
    
    def onRockBreak(self):
        SOUND_SMOT.play()

    def onOreHit(self):
        SOUND_SMOT.play()
    
    def onOreBreak(self):
        SOUND_SMOT.play()
        SOUND_POINT.play()
        
    def onSlimeHit(self):
        SOUND_HIT2.play()

    def onSlimeDead(self):
        SOUND_HIT.play()
    
    def onPlayerHit(self):
        SOUND_HIT2.play()

    def onPlayerDead(self):
        SOUND_HIT.play()

    def onBuy(self):
        SOUND_POINT.play()

    def onStep(self):
        SOUND_FOOTSTEP.play()

    def onJump(self):
        SOUND_FOOTSTEP.play()
    
    def onDrop(self):
        SOUND_FOOTSTEP.play()



audio = Audio()

