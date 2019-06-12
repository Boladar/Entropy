import math
import constants
import random

class Particle:

    def __init__(self, x, y, vx, vy):

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = 1

    def wall(self):
        if self.x < constants.PARTICLE_RADIUS:
            self.x = 2 * constants.PARTICLE_RADIUS - self.x
            self.vx *= -1
        if self.x > constants.WORLD_SIZE-constants.PARTICLE_RADIUS:
            self.x = 2 * (constants.WORLD_SIZE - constants.PARTICLE_RADIUS) - self.x
            self.vx *=-1
        if self.y < constants.PARTICLE_RADIUS:
            self.y = 2 * constants.PARTICLE_RADIUS - self.y
            self.vy *= -1
        if self.y > constants.WORLD_SIZE-constants.PARTICLE_RADIUS:
            self.y = 2 * (constants.WORLD_SIZE - constants.PARTICLE_RADIUS) - self.y
            self.vy *=-1

    def collision(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        dist = math.sqrt(dx * dx + dy * dy)
        if dist <= 2 * constants.PARTICLE_RADIUS:
            angle_collision = math.atan2((p.y-self.y),(p.x-self.x))

            V = math.sqrt((self.vx ** 2) + (self.vy ** 2))
            angle1 = math.atan2(self.vy, self.vx)

            Vp = math.sqrt((p.vx ** 2) + (p.vy ** 2))
            angle2 = math.atan2(p.vy, p.vx)

            Vx1 = V * math.cos(angle1 - angle_collision)
            Vy1 = V * math.sin(angle1 - angle_collision)

            Vx2 = Vp * math.cos(angle2 - angle_collision)
            Vy2 = Vp * math.sin(angle2 - angle_collision)

            Vx1, Vx2 = Vx2, Vx1

            cos_convert = math.cos(angle_collision)
            sin_convert = math.sin(angle_collision)

            self.vx = cos_convert * Vx1 - sin_convert * Vy1
            self.vy = sin_convert * Vx1 + cos_convert * Vy1

            p.vx = cos_convert * Vx2 - sin_convert * Vy2
            p.vy = sin_convert * Vx2 + cos_convert * Vy2

            overlap = 0.5 * (dist - 2 * constants.PARTICLE_RADIUS)
            self.x -= overlap * (self.x - p.x) / dist
            self.y -= overlap * (self.y - p.y) / dist
            p.x += overlap * (self.x - p.x) / dist
            p.x += overlap * (self.y - p.y) / dist

    def move(self):
        self.x+=(self.vx*constants.TIME_STEP)
        self.y+=(self.vy*constants.TIME_STEP)