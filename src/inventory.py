import pygame

class Inventory:
    def __init__(self):
        self.open = False
        self.player = None
        self.cost = 5

    def update(self):
        self.clopen_inventory()

    def clopen_inventory(self):
        self.open = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.open = True

    def upgrade_atk_strength(self):
        if self.player.score > self.cost:
            self.player.atk_strength += 1
            self.cost += 5
        
    def upgrade_atk_speed(self):
        if self.player.score > self.cost:
            self.cost += 5
            self.player.atk_speed -= 2

    def upgrade_atk_range(self):
        if self.player.score > self.cost:
            self.cost += 5
            self.player.atk_range += 3000

    def upgrade_block_break(self):
        pass

    def render(self, screen):
        if self.open:
            pass

        