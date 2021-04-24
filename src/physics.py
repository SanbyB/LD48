import pygame

class Physics:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.x_hit, self.y_hit = 0, 0 
        self.x_vel = 0
        self.y_vel = 0
        self.grav = 0.3

    def update(self):
        self.gravity()
        self.resolveCollisions()
        self.applyVelocity()


    def gravity(self):
        self.y_vel += self.grav

    
    def hit_box(self, name):
        im_size = name.get_width(), name.get_height()
        return im_size


    def resolveCollisions(self):
        
        # Does right side collide
        if self.x_vel > 0 and self.world.tileMap.doesCollide(self.x + self.x_vel + self.width, self.y + self.height / 2):

            self.x_vel = 0
            self.onHitEdge()

        # Does left side collide
        if self.x_vel < 0 and self.world.tileMap.doesCollide(self.x + self.x_vel, self.y + self.height / 2):
            self.x_vel = 0
            self.onHitEdge()
        
        # Does bottom collide
        if self.y_vel > 0 and self.world.tileMap.doesCollide(self.x + self.width / 2, self.y + self.height + self.y_vel):
            if self.y_vel < 2.5:
                self.y_vel = 0
            self.y_vel = -self.y_vel * 0.8
            self.onHitFloor()
            

        # Does top collide
        if self.y_vel < 0 and self.world.tileMap.doesCollide(self.x + self.width / 2, self.y + self.y_vel):
            self.y_vel = -self.y_vel * 0.08
            self.onHitRoof()

        return

    def applyVelocity(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.x_vel = self.x_vel * 0.93
        self.y_vel = self.y_vel * 0.97




    def onHitEdge(self):
        return

    def onHitFloor(self):
        return

    def onHitRoof(self):
        return


        

