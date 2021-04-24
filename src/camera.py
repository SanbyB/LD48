

class Camera:
    def __init__(self):
        self.x, self.y = 0, 0

    def move(self, player):
        self.x = player.x
        self.y = player.y
        print(self.x, self.y)