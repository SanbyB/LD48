from config import SCREEN_HEIGHT, SCREEN_WIDTH

class Camera:
    def __init__(self):
        self.x, self.y = 0, 0

    def move(self, player):
        self.x = player.x - (SCREEN_WIDTH / 2) + (player.width / 2)
        self.y = player.y - (SCREEN_HEIGHT / 2) + (player.height / 2)