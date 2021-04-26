import pygame
from config import SCREEN_HEIGHT, SCREEN_WIDTH
from resources import  EVEN_SMALLER_FONT


WINDOW_WIDTH, WINDOW_HEIGHT = SCREEN_WIDTH/1.3, SCREEN_HEIGHT/1.5
WINDOW = (SCREEN_WIDTH/2 - WINDOW_WIDTH/2, SCREEN_HEIGHT/2 - WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT)
BUTTON1 = (SCREEN_WIDTH/2 - (WINDOW_WIDTH/2 * 0.9), SCREEN_HEIGHT/2 - (WINDOW_HEIGHT/2 * 0.9), WINDOW_WIDTH*0.4, WINDOW_HEIGHT*0.4)
BUTTON2 = (SCREEN_WIDTH/2 - (WINDOW_WIDTH/2 * 0.9), SCREEN_HEIGHT/2 + (WINDOW_HEIGHT/2 * 0.1), WINDOW_WIDTH*0.4, WINDOW_HEIGHT*0.4)
BUTTON3 = (SCREEN_WIDTH/2 + (WINDOW_WIDTH/2 * 0.1), SCREEN_HEIGHT/2 - (WINDOW_HEIGHT/2 * 0.9), WINDOW_WIDTH*0.4, WINDOW_HEIGHT*0.4)
BUTTON4 = (SCREEN_WIDTH/2 + (WINDOW_WIDTH/2 * 0.1), SCREEN_HEIGHT/2 + (WINDOW_HEIGHT/2 * 0.1), WINDOW_WIDTH*0.4, WINDOW_HEIGHT*0.4)


class Inventory:
    def __init__(self):
        self.open = False
        self.not_opened = True
        self.player = None
        self.strength_cost = 5
        self.speed_cost = 5
        self.range_cost = 3
        self.health_cost = 2
        self.click = True
        self.strength_max = False
        self.speed_max = False
        self.range_max = False
        self.health_max = True

    def update(self):
        self.clopen_inventory()
        self.buy()
        if self.player.hp <= 15:
            self.health_max = False
        else:
            self.health_max = True

    def clopen_inventory(self):
        self.open = False
        keys = pygame.key.get_pressed()

        if keys[pygame.K_e]:
            self.open = True
            self.not_opened = False

    def upgrade_atk_strength(self):
        if self.player.atk_strength < 8:
            if self.player.score >= self.strength_cost:
                self.player.score -= self.strength_cost
                self.player.atk_strength += 1
                self.strength_cost += 3
        else:
            self.strength_max = True
        
    def upgrade_atk_speed(self):
        if self.player.atk_speed > 15:
            if self.player.score >= self.speed_cost:
                self.player.score -= self.speed_cost
                self.speed_cost += 2
                self.player.atk_speed -= 3
        else:
            self.speed_max = True

    def upgrade_atk_range(self):
        if self.player.atk_range < 50000:
            if self.player.score >= self.range_cost:
                self.player.score -= self.range_cost
                self.range_cost += 2
                self.player.atk_range += 3000
        else:
            self.range_max = True

    def recover_health(self):
        if self.player.hp <= 15:
            if self.player.score >= self.health_cost:
                self.player.score -= self.health_cost
                self.health_cost += 1
                self.player.hp += 5


    def text(self, surface):
        img1 = EVEN_SMALLER_FONT.render("Upgrade", True, (255, 255, 255))
        img2 = EVEN_SMALLER_FONT.render("AtTaCk", True, (255, 255, 255))
        img20 = EVEN_SMALLER_FONT.render("AtTaCk  and", True, (255, 255, 255))
        img3 = EVEN_SMALLER_FONT.render("strength", True, (255, 255, 255))
        img4 = EVEN_SMALLER_FONT.render("range", True, (255, 255, 255))
        img5 = EVEN_SMALLER_FONT.render("mining  speed", True, (255, 255, 255))
        img6 = EVEN_SMALLER_FONT.render("recover", True, (255, 255, 255))
        img7 = EVEN_SMALLER_FONT.render("health", True, (255, 255, 255))
        img70 = EVEN_SMALLER_FONT.render("health", True, (0, 0, 0))

        c1 = c2 = c3 = c4 = (0, 0, 0, 0)

        if self.strength_cost <= self.player.score:
            c1 = (255, 255, 255)

        if self.range_cost <= self.player.score:
            c2 = (255, 255, 255)

        if self.speed_cost <= self.player.score:
            c3 = (255, 255, 255)

        if self.health_cost <= self.player.score:
            c4 = (255, 255, 255)


        img8 = EVEN_SMALLER_FONT.render("cost      " + str(self.strength_cost), True, c1)
        img9 = EVEN_SMALLER_FONT.render("cost      " + str(self.range_cost), True, c2)
        img10 = EVEN_SMALLER_FONT.render("cost      " + str(self.speed_cost), True, c3)
        img11 = EVEN_SMALLER_FONT.render("cost      " + str(self.health_cost), True, c4)

        img12 = EVEN_SMALLER_FONT.render("Fully", True, (0, 0, 0))
        img13 = EVEN_SMALLER_FONT.render("Upgraded", True, (0, 0, 0))
        img14 = EVEN_SMALLER_FONT.render("too  high", True, (0, 0, 0))

        width1 = img1.get_width()
        height1 = img1.get_height()
        
        width2 = img6.get_width()
        height2 = img6.get_height()

        width3 = img12.get_width()
        height3 = img12.get_height()

        width4 = img7.get_width()
        height4 = img7.get_height()                                


        if self.strength_max:
            surface.blit(img12, (BUTTON1[0] + width3 * 0.2, BUTTON1[1] + height3))
            surface.blit(img13, (BUTTON1[0] + width3 * 0.2, BUTTON1[1] + height3*2.5))

        else:
            surface.blit(img1, (BUTTON1[0] + width1 * 0.2, BUTTON1[1]))
            surface.blit(img2, (BUTTON1[0] + width1 * 0.2, BUTTON1[1] + height1))
            surface.blit(img3, (BUTTON1[0] + width1 * 0.2, BUTTON1[1] + height1 * 2))
            surface.blit(img8, (BUTTON1[0] + width1 * 0.3, BUTTON1[1] + height1 * 3.2))



        if self.range_max:
            surface.blit(img12, (BUTTON2[0] + width1 * 0.2, BUTTON2[1] + height3))
            surface.blit(img13, (BUTTON2[0] + width3 * 0.2, BUTTON2[1] + height3*2.5))

        else:
            surface.blit(img1, (BUTTON2[0] + width1 * 0.2, BUTTON2[1]))
            surface.blit(img2, (BUTTON2[0] + width1 * 0.2, BUTTON2[1] + height1))
            surface.blit(img4, (BUTTON2[0] + width1 * 0.2, BUTTON2[1] + height1 * 2))
            surface.blit(img9, (BUTTON2[0] + width1 * 0.3, BUTTON2[1] + height1 * 3.2))



        if self.speed_max:
            surface.blit(img12, (BUTTON3[0] + width3 * 0.1, BUTTON3[1] + height3))
            surface.blit(img13, (BUTTON3[0] + width3 * 0.1, BUTTON3[1] + height3*2.5))

        else:
            surface.blit(img1, (BUTTON3[0] + width1 * 0.1, BUTTON3[1]))
            surface.blit(img20, (BUTTON3[0] + width1 * 0.1, BUTTON3[1] + height1))
            surface.blit(img5, (BUTTON3[0] + width1 * 0.1, BUTTON3[1] + height1 * 2))
            surface.blit(img10, (BUTTON3[0] + width1 * 0.3, BUTTON3[1] + height1 * 3.2))



        if self.health_max:
            surface.blit(img70, (BUTTON4[0] + width4 * 0.2, BUTTON4[1]+ height4))
            surface.blit(img14, (BUTTON4[0] + width4 * 0.2, BUTTON4[1] + height4*2.5))


        else:
            surface.blit(img6, (BUTTON4[0] + width2 * 0.2, BUTTON4[1]+ height2*0.5))
            surface.blit(img7, (BUTTON4[0] + width2 * 0.2, BUTTON4[1] + height2*1.5))
            surface.blit(img11, (BUTTON4[0] + width2 * 0.2, BUTTON4[1] + height2 * 3.2))
        
        return



    def render(self, screen):
        if self.not_opened:
            img = EVEN_SMALLER_FONT.render("Press  e  to  open  inventory", True, (255, 255, 255))
            width = img.get_width()
            height = img.get_height()

            pygame.draw.rect(screen, (0, 0, 0), (0, SCREEN_HEIGHT - height, width, height))
            screen.blit(img, (0, SCREEN_HEIGHT - height))

        if self.open:
            pygame.draw.rect(screen, (186, 183, 175), WINDOW)

            pygame.draw.rect(screen, (112, 77, 56),  BUTTON1)
            pygame.draw.rect(screen, (112, 77, 56),  BUTTON2)
            pygame.draw.rect(screen, (112, 77, 56),  BUTTON3)
            pygame.draw.rect(screen, (112, 77, 56),  BUTTON4)

            self.text(screen)


    def buy(self):
        if self.open:
            mouse = pygame.mouse.get_pressed()

            if mouse[0] == 1:
                if self.click:
                    mp = pygame.mouse.get_pos()
                    if BUTTON1[0] < mp[0] < BUTTON1[0] + BUTTON1[2] and BUTTON1[1] < mp[1] < BUTTON1[1] + BUTTON1[3]:
                        self.upgrade_atk_strength()
                    
                    if BUTTON2[0] < mp[0] < BUTTON2[0] + BUTTON2[2] and BUTTON2[1] < mp[1] < BUTTON2[1] + BUTTON2[3]:
                        self.upgrade_atk_range()

                    if BUTTON3[0] < mp[0] < BUTTON3[0] + BUTTON3[2] and BUTTON3[1] < mp[1] < BUTTON3[1] + BUTTON3[3]:
                        self.upgrade_atk_speed()

                    if BUTTON4[0] < mp[0] < BUTTON4[0] + BUTTON4[2] and BUTTON4[1] < mp[1] < BUTTON4[1] + BUTTON4[3]:
                        self.recover_health()

                self.click = False
            
            else:
                self.click = True
            

            