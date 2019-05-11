
class Particle:

    def __init__(self,x,y,Vx,Vy):

        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy

def wall(self):
    if self.x > width - self.size:
        self.x = 2 * (width - size) - self.x
        self.Vx = -self.Vx
    
    elif self.x < self.size:
        self.x = 2 * size - self.x
        self.Vx = -self.Vx
    
    if self.y > height - self.size:
        self.y = 2 * (height - size) - self.y
        self.Vy = -self.Vy
    
    elif self.y < self.size:
        self.y = 2 * size - self.y
        self.Vy = -self.Vy

    def Update(self):
        pass
