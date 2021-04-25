
from math import floor

class Animation:
    def __init__(self, spritesheet, rowIndex, speed):
        self.spritesheet = spritesheet
        self.rowIndex = rowIndex
        self.frame = 0
        self.speed = speed
        return


    def update(self):
        self.frame += self.speed
        return

    def draw(self, surface, x, y, width, height, direction):
        frame = floor(self.frame) % self.spritesheet.xFrames
        frame = self.spritesheet.xFrames - 1 - frame if direction else frame
        self.spritesheet.draw(
            surface,
            frame,
            self.rowIndex,
            x, y, width, height,
            direction
        )
        return

    def reset(self):
        self.frame = 0




