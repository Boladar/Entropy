import constants
import random
import math
from particle import Particle


class World:

    def __init__(self,Size):
        self.Size = Size
        self.particles = []

        for i in range(constants.NUMBER_OF_PARTICLES):
            x = random.randint(10, 100)
            y = random.randint(10, self.Size - 10)
            vx = random.uniform(-constants.MAX_SPEED,constants.MAX_SPEED)
            vy = random.uniform(-constants.MAX_SPEED,constants.MAX_SPEED)
            if (i != 0):
                for j in self.particles:
                    while(math.sqrt((j.x - x)*(j.x - x)+(j.y - y)*(j.y - y))<constants.PARTICLE_RADIUS*2):
                        x = random.randint(10, 100)
                        y = random.randint(10, constants.WORLD_SIZE - 10)
            self.particles.append(Particle(x, y, vx, vy))

    def number_of_particles(self):
        descreet_world = []
        sum = 0
        for i in range(20,820,20):
            for j in range(20,820,20):
                for p in self.particles:
                    if p.y >= j - 20 and p.y <= j and p.x >= i - 20 and p.x <= i:
                        sum += 1
            descreet_world.append(sum)
            sum = 0
        return descreet_world

    def therm_prob(self):
        descreet_world = self.number_of_particles()
        power_of_eap = constants.NUMBER_OF_PARTICLES * math.log1p(
            constants.NUMBER_OF_PARTICLES) - constants.NUMBER_OF_PARTICLES
        for i in descreet_world:
            power_of_en = i * math.log1p(i) - i
            power_of_eap -= power_of_en
        return "Thermodynamics probability is e to the power of {}".format(int(power_of_eap))

    def entropy(self):
        descreet_world = self.number_of_particles()
        self.entropy_array = []
        power_of_eap = constants.NUMBER_OF_PARTICLES * math.log1p(constants.NUMBER_OF_PARTICLES) - constants.NUMBER_OF_PARTICLES
        for i in descreet_world:
            power_of_en = i * math.log1p(i) - i
            power_of_eap -= power_of_en
        return power_of_eap

    def update(self):
        for p1 in self.particles:
            p1.move()
            p1.wall()
            for p2 in self.particles:
                if p1 != p2:
                    p1.collision(p2)




