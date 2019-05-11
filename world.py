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

        for i in range(constants.NUMBER_OF_PARTICLES):
            self.particles.append(Particle(0,i,random.randint(-constants.MAX_SPEED,constants.MAX_SPEED),random.randint(-constants.MAX_SPEED,constants.MAX_SPEED)))


    def update(self):
        self.tiles.clear()
        self.create_world_dictionary()

        for p in self.particles:
            collision_array = self.create_collision_array(p)
            p.update(collision_array)
            


    def create_world_dictionary(self):
        
        for p in self.particles:
            self.assign_tile(p)

    def create_collision_array(self,particle):
        
        collision_array = []
        tile_coordinates = self.get_tile_coordinates(particle)

        x = tile_coordinates[0]
        y = tile_coordinates[1]

        for i in range(-1,1):
            for j in range(-1,1):
                tile_hash = self.tile_hash(x+i,y+j)

                if tile_hash in self.tiles:
                    collision_array = collision_array + self.tiles[tile_hash].particles

        return collision_array

    def tile_hash(self,x,y):
        return hash('{},{}'.format(x,y))

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