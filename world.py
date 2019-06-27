import constants
import random
import math
from particle import Particle


class World:

    def __init__(self, Size):
        self.Size = Size
        self.particles = []
        self.states = dict()
        self.W = 0
        self.step = 500

        for i in range(constants.NUMBER_OF_PARTICLES):
            x = random.randint(10, 150)
            y = random.randint(10, self.Size - 10)
            vx = random.uniform(-constants.MAX_SPEED, constants.MAX_SPEED)
            vy = random.uniform(-constants.MAX_SPEED, constants.MAX_SPEED)
            self.W += (vx*vx + vy*vy)
            if i != 0:
                for j in self.particles:
                    while math.sqrt((j.x - x)*(j.x - x)+(j.y - y)*(j.y - y)) < constants.PARTICLE_RADIUS*2:
                        x = random.randint(10, 100)
                        y = random.randint(10, constants.WORLD_SIZE - 10)
            self.particles.append(Particle(x, y, vx, vy))

        self.W = math.sqrt(self.W) / (2 * constants.NUMBER_OF_PARTICLES)
        self.W = ((self.W // 500) + 1) * 500



    def all_states(self):
        position = []
        velocity = []
        self.W = int(self.W)


        for i in range(0, constants.WORLD_SIZE, 200):
            for j in range(0, constants.WORLD_SIZE, 200):
                position.append([i, j])

        for i in range(-self.W, self.W, self.step):
            for j in range(-self.W, self.W, self.step):
                velocity.append([i, j])

        for i1, i2 in position:
            for j1, j2 in velocity:
                self.states["[{},{},{},{}]".format(i1, i2, j1, j2)] = 0

    def compute_state(self):
        for p in self.particles:
            if p.x < 0:
                p.x *= -1
            if p.y < 0:
                p.y *= -1

            x = int(p.x) // 200
            y = int(p.y) // 200
            vx = (int(p.vx) // self.step)
            vy = (int(p.vy) // self.step)

            x *= 200
            y *= 200
            vx *= self.step
            vy *= self.step

            self.states["[{},{},{},{}]".format(x, y, vx, vy)] += 1


    def particle_positions(self):
        for i, p in enumerate(self.particles):
            print("Particle {} position XY: ({},{}) and position Vxy: ({},{})".format(i, int(p.x), int(p.y), int(p.vx), int(p.vy)))

    def entropy(self):
        states = self.states.items()
        power_of_eap = constants.NUMBER_OF_PARTICLES * math.log1p(constants.NUMBER_OF_PARTICLES) - constants.NUMBER_OF_PARTICLES
        for k, v in states:
            power_of_en = (v * math.log1p(v)) - v
            power_of_eap -= power_of_en
            self.states[k] = 0
        return power_of_eap


    def update(self):
        for p1 in self.particles:
            p1.move()
            p1.wall()
            for p2 in self.particles:
                if p1 != p2:
                    p1.collision(p2, self.W)
