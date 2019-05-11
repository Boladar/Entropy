import constants
import random
import math
from particle import Particle
from tile import Tile
class World:

    def __init__(self,N,R):
        self.N = N
        self.R = R

        self.Particles = []
        self.Tiles = set()

        for i in range(constants.WORLD_SIZE):
            self.Particles.append(Particle(0,i,random.randint(-constants.MAX_SPEED,constants.MAX_SPEED),random.randint(-constants.MAX_SPEED,constants.MAX_SPEED)))


    def update(self):
        pass

    def create_world_array(self):
        pass

    def assign_tile(self,particle):
        coordinates = self.get_tile_coordinates(particle)
        particle_tile = Tile(coordinates[0],coordinates[1])


    def get_tile_coordinates(self,particle):
        x = math.floor(particle.x)
        y = math.floor(particle.y)

        return [x,y]

    def create_collision_array(self, particle):
        pass