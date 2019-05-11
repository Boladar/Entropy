import constants
import random
import math
from particle import Particle
from tile import Tile
class World:

    def __init__(self,N,R):
        self.N = N
        self.R = R

        self.particles = []
        self.tiles = {}

        for i in range(constants.WORLD_SIZE):
            self.particles.append(Particle(0,i,random.randint(-constants.MAX_SPEED,constants.MAX_SPEED),random.randint(-constants.MAX_SPEED,constants.MAX_SPEED)))


    def update(self):
        pass

    def create_world_array(self):
        
        for p in self.particles:
            self.assign_tile(p)

    def create_collision_array(self,particle):
        
        collision_array = []
        tile_coordinates = self.get_tile_coordinates(particle)
        tile_hash = hash(tile_coordinates[0] + tile_coordinates[1])

        


    def assign_tile(self,particle):
        coordinates = self.get_tile_coordinates(particle)
        particle_tile = Tile(coordinates[0],coordinates[1])

        if particle_tile.__hash__() in self.tiles:
            self.tiles[particle_tile.__hash__()].particles.append(particle)
        else:
            particle_tile.particles.append(particle)
            self.tiles[particle_tile.__hash__()] = particle_tile


    def get_tile_coordinates(self,particle):
        x = math.floor(particle.x)
        y = math.floor(particle.y)

        return [x,y]