from resources import FONT, SMALLER_FONT
from config import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame

class UI:
    def __init__(self, world):
        self.world = world

    def draw(self, surface):
        img2 = FONT.render(str(self.world.player.score), True, (255, 255, 255))
        width = img2.get_width()
        height = img2.get_height()
        surface.blit(img2, (SCREEN_WIDTH/2 - width/2, 0))
        return


    def renderStartingScreen(self, surface):
        img = FONT.render("Craftmine", True, (200, 200, 200))
        width = img.get_width()
        height = img.get_height()

        img2 = FONT.render("Press  Enter", True, (255, 255, 255))
        width2 = img2.get_width()
        height2 = img2.get_height()

        img3 = FONT.render("To  Start", True, (255, 255, 255))
        width3 = img3.get_width()
        height3 = img3.get_height()

        pygame.draw.rect(surface, (0, 0, 0), (100, 100, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200))
        surface.blit(img, (SCREEN_WIDTH/2 - width/2, SCREEN_HEIGHT/2 - height/2 - height2))
        surface.blit(img2, (SCREEN_WIDTH/2 - width2/2, SCREEN_HEIGHT/2 - height2/2))
        surface.blit(img3, (SCREEN_WIDTH/2 - width3/2, SCREEN_HEIGHT/2 - height3/2 + height2))
        return

    def renderDiedScreen(self, surface, highScore):
        img = FONT.render("You  died", True, (200, 200, 200))
        width = img.get_width()
        height = img.get_height()

        img2 = SMALLER_FONT.render("Your  high  score  is", True, (255, 255, 255))
        width2 = img2.get_width()
        height2 = img2.get_height()

        img3 = SMALLER_FONT.render(str(highScore) + "  points", True, (255, 255, 255))
        width3 = img3.get_width()
        height3 = img3.get_height()

        img4 = SMALLER_FONT.render("Press  Enter  to  restart", True, (255, 255, 255))
        width4 = img4.get_width()
        height4 = img4.get_height()

        pygame.draw.rect(surface, (0, 0, 0), (100, 100, SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200))
        surface.blit(img, (SCREEN_WIDTH/2 - width/2, SCREEN_HEIGHT/2 - height/2 - height2 - 50))
        surface.blit(img2, (SCREEN_WIDTH/2 - width2/2, SCREEN_HEIGHT/2 - height2/2))
        surface.blit(img3, (SCREEN_WIDTH/2 - width3/2, SCREEN_HEIGHT/2 - height3/2 + height2))
        surface.blit(img4, (SCREEN_WIDTH/2 - width4/2, SCREEN_HEIGHT/2 - height4/2 + height2 + height3 + 30))
        return

