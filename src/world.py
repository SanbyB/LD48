
class World:
    def __init__(self): 
        self.entities = []
        self.toAdd = []
        self.toRemove = []


    def update(self):  
        for entityToAdd in self.toAdd:
            self.entities.append(entityToAdd)
        for entityToRemove in self.toRemove:
            self.entities.remove(entityToRemove)
        self.toAdd.clear();
        self.toRemove.clear();
        for entity in self.entities:
            entity.update()


    def render(self):    
        for entity in self.entities:
            entity.render()

    def addEntity(self, entity):
        self.toAdd.append(entity)

    def removeEntity(self, entity):
        self.toRemove.append(entity)


