from resources import FONT
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class UI:
    def __init__(self, world):
        self.world = world

    def draw(self, surface):
        img2 = FONT.render(str(self.world.player.score), True, (255, 255, 255))
        width = img2.get_width()
        height = img2.get_height()
        surface.blit(img2, (SCREEN_WIDTH/2 - width/2, 0))
        return

