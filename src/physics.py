import pygame

class Physics:
    def __init__(self, x, y, width, height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.x_vel = 0
        self.y_vel = 0
        self.grav = 0.3

    def update(self):
        self.gravity()
        self.resolveCollisions()
        self.applyVelocity()


    def gravity(self):
        self.y_vel += self.grav


    def resolveCollisions(self):
        
        # Does right side collide
        if self.x_vel > 0 and self.world.tileMap.doesCollide(self.x + self.x_vel + self.width, self.y):
            self.x_vel = 0
            self.onHitEdge()
        if self.x_vel > 0 and self.world.tileMap.doesCollide(self.x + self.x_vel + self.width, self.y + self.height):
            self.x_vel = 0
            self.onHitEdge()

        # Does left side collide
        if self.x_vel < 0 and self.world.tileMap.doesCollide(self.x + self.x_vel, self.y):
            self.x_vel = 0
            self.onHitEdge()
        if self.x_vel < 0 and self.world.tileMap.doesCollide(self.x + self.x_vel, self.y + self.height):
            self.x_vel = 0
            self.onHitEdge()
        
        
        BOTTOM_FRIC = 0.5
        # Does bottom collide
        if self.y_vel > 0 and self.world.tileMap.doesCollide(self.x, self.y + self.height + self.y_vel):
            if self.y_vel < 2.5:
                self.y_vel = 0
            self.y_vel = -self.y_vel * BOTTOM_FRIC
            self.onHitFloor()
        if self.y_vel > 0 and self.world.tileMap.doesCollide(self.x + self.width, self.y + self.height + self.y_vel):
            if self.y_vel < 2.5:
                self.y_vel = 0
            self.y_vel = -self.y_vel * BOTTOM_FRIC
            self.onHitFloor()

        # Does top collide
        if self.y_vel < 0 and self.world.tileMap.doesCollide(self.x, self.y + self.y_vel):
            self.y_vel = -self.y_vel * 0.08
            self.onHitRoof()
        if self.y_vel < 0 and self.world.tileMap.doesCollide(self.x + self.width, self.y + self.y_vel):
            self.y_vel = -self.y_vel * 0.08
            self.onHitRoof()

        return

    def applyVelocity(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.x_vel = self.x_vel * 0.8
        self.y_vel = self.y_vel * 0.97




    def onHitEdge(self):
        return

    def onHitFloor(self):
        return

    def onHitRoof(self):
        return


        

