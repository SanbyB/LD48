from maps.tilemap import TileMap

class World:
    def __init__(self):
        self.player = None 
        self.entities = []
        self.toAdd = []
        self.toRemove = []
        self.tileMap = TileMap(self, self.onGenerateListener)


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
        self.tileMap.render(surface, camera) 
        for entity in self.entities:
            entity.render(surface, camera)

    def addEntity(self, entity):
        self.toAdd.append(entity)

    def removeEntity(self, entity):
        self.toRemove.append(entity)


    # This is called when the camera causes the map to increase in size
    # We should generate enemies and things in this function
    # Index, measured in tile count of how deep the world is 
    def onGenerateListener(self, index):
        #print("Generated world", index, "deep")
        return


