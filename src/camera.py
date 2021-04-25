from config import SCREEN_HEIGHT, SCREEN_WIDTH
import random

class Camera:
    def __init__(self):
        self.x, self.y = 0, 0
        self.shakeAmount = 0

    def move(self, player):
        self.x = (player.x - (SCREEN_WIDTH / 2) + (player.width / 2)) + random.uniform(0, self.shakeAmount)
        self.y = (player.y - (SCREEN_HEIGHT / 2) + (player.height / 2)) + random.uniform(0, self.shakeAmount)
        self.shakeAmount = self.shakeAmount * 0.9

    def shake(self, amount):
        self.shakeAmount += amount