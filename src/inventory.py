import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH


WINDOW_WIDTH, WINDOW_HEIGHT = SCREEN_WIDTH/1.3, SCREEN_HEIGHT/1.5
WINDOW = (SCREEN_WIDTH/2 - WINDOW_WIDTH/2, SCREEN_HEIGHT/2 - WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT)
BUTTON1 = (SCREEN_WIDTH/2 - (WINDOW_WIDTH/2 * 0.9), SCREEN_HEIGHT/2 - (WINDOW_HEIGHT/2 * 0.9), WINDOW_WIDTH*0.4, WINDOW_HEIGHT*0.4)
BUTTON2 = (SCREEN_WIDTH/2 - (WINDOW_WIDTH/2 * 0.9), SCREEN_HEIGHT/2 + (WINDOW_HEIGHT/2 * 0.1), WINDOW_WIDTH*0.4, WINDOW_HEIGHT*0.4)
BUTTON3 = (SCREEN_WIDTH/2 + (WINDOW_WIDTH/2 * 0.1), SCREEN_HEIGHT/2 - (WINDOW_HEIGHT/2 * 0.9), WINDOW_WIDTH*0.4, WINDOW_HEIGHT*0.4)
BUTTON4 = (SCREEN_WIDTH/2 + (WINDOW_WIDTH/2 * 0.1), SCREEN_HEIGHT/2 + (WINDOW_HEIGHT/2 * 0.1), WINDOW_WIDTH*0.4, WINDOW_HEIGHT*0.4)


class Inventory:
    def __init__(self):
        self.open = False
        self.player = None
        self.cost = 5

    def update(self):
        self.clopen_inventory()
        self.buy()

    def clopen_inventory(self):
        self.open = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.open = True

    def upgrade_atk_strength(self):
        if self.player.atk_strength < 8:
            if self.player.score >= self.cost:
                self.player.score -= self.cost
                self.player.atk_strength += 1
                self.cost += 5
        
    def upgrade_atk_speed(self):
        if self.player.atk_speed > 15:
            if self.player.score >= self.cost:
                self.player.score -= self.cost
                self.cost += 5
                self.player.atk_speed -= 2

    def upgrade_atk_range(self):
        if self.player.atk_range < 50000:
            if self.player.score >= self.cost:
                self.player.score -= self.cost
                self.cost += 5
                self.player.atk_range += 3000

    def recover_health(self):
        if self.player.hp <= 15:
            if self.player.score >= self.cost:
                self.player.score -= self.cost
                self.cost += 5
                self.player.hp += 5

    def render(self, screen):
        if self.open:
            pygame.draw.rect(screen, (186, 183, 175), WINDOW)

            pygame.draw.rect(screen, (112, 77, 56),  BUTTON1)
            pygame.draw.rect(screen, (112, 77, 56),  BUTTON2)
            pygame.draw.rect(screen, (112, 77, 56),  BUTTON3)
            pygame.draw.rect(screen, (112, 77, 56),  BUTTON4)

    def buy(self):
        if self.open:
            mouse = pygame.mouse.get_pressed()

            if mouse[0] == 1:
                mp = pygame.mouse.get_pos()
                if BUTTON1[0] < mp[0] < BUTTON1[0] + BUTTON1[2] and BUTTON1[1] < mp[1] < BUTTON1[1] + BUTTON1[3]:
                    self.upgrade_atk_strength()
                
                if BUTTON2[0] < mp[0] < BUTTON2[0] + BUTTON2[2] and BUTTON2[1] < mp[1] < BUTTON2[1] + BUTTON2[3]:
                    self.upgrade_atk_range()

                if BUTTON3[0] < mp[0] < BUTTON3[0] + BUTTON3[2] and BUTTON3[1] < mp[1] < BUTTON3[1] + BUTTON3[3]:
                    self.upgrade_atk_speed()

                if BUTTON4[0] < mp[0] < BUTTON4[0] + BUTTON4[2] and BUTTON4[1] < mp[1] < BUTTON4[1] + BUTTON4[3]:
                    self.recover_health()
            

            