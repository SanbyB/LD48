from maps.tilemap import TileMap
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from maps.tilemap import TILE_MAP_WIDTH, TILE_SIZE 

class World:
    def __init__(self, camera):
        self.player = None
        self.camera = camera 
        self.entities = []
        self.toAdd = []
        self.toRemove = []
        self.tileMap = TileMap(self)


    def update(self, camera):  
        for entityToAdd in self.toAdd:
            self.entities.append(entityToAdd)
        for entityToRemove in self.toRemove:
            self.entities.remove(entityToRemove)
        self.toAdd.clear();
        self.toRemove.clear();
        for entity in self.entities:
            entity.update(camera)


    def render(self, surface, camera):   
        
        camX = camera.x
        camRight = camera.x + SCREEN_WIDTH
        if camX < 0:
            camX = 0
        if camRight > TILE_MAP_WIDTH * TILE_SIZE:
            camRight = TILE_MAP_WIDTH * TILE_SIZE

        

        pygame.draw.rect(surface, (28, 22, 27), (camX - camera.x, 0, (camRight - camX), SCREEN_HEIGHT))


        self.player.render(surface, camera)
        self.tileMap.render(surface, camera) 
        for entity in self.entities:
            entity.render(surface, camera)

    def addEntity(self, entity):
        self.toAdd.append(entity)

    def removeEntity(self, entity):
        self.toRemove.append(entity)




