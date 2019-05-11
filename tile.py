
class Tile:

    def __init__(self,x,y):
        self.x = x 
        self.y = y
        self.particles = []


    def __hash__(self):
        return hash('{},{}'.format(self.x,self.y))

    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
