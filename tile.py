
class Tile:

    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.Particles = []


    def __hash__(self):
        return hash(self.x + self.y)