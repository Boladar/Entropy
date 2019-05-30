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

    def one_dimention(self,p,angle):
        x1 = self.vx * math.cos(angle) - self.vy * math.sin(angle)
        y1 = self.vx * math.sin(angle) + self.vy * math.cos(angle)
        x2 = p.vx * math.cos(angle) - p.vy * math.sin(angle)
        y2 = p.vx * math.sin(angle) + p.vy * math.cos(angle)
        return [x1,y1,x2,y2]

    def collision(self, p):
        #for p in collision_array:
            dx = self.x - p.x
            dy = self.y - p.y
            dist = math.sqrt(dx * dx + dy * dy)
            if dist <= 2 * constants.PARTICLE_RADIUS and self.x != p.x and self.y != p.y:
                overlap = 0.5 * (dist - 2 * constants.PARTICLE_RADIUS)
                self.x -= overlap * (self.x - p.x) / dist
                self.y -= overlap * (self.y - p.y) / dist
                p.x += overlap * (self.x - p.x) / dist
                p.x += overlap * (self.y - p.y) / dist

                angle = - math.atan2(p.y - self.y, p.x - self.x)

                u1 = self.one_dimention(p, angle)

                self.vx = (u1[0] * (self.mass - p.mass) + 2.0 * u1[2] * p.mass) / (self.mass + p.mass)
                self.vy = u1[1]
                p.vx = (u1[2] * (self.mass - p.mass) + 2.0 * u1[0] * p.mass) / (self.mass + p.mass)
                p.vy = u1[3]

                u2 = self.one_dimention(self, -angle)

                self.vx = u2[0]
                self.vy = u2[1]
                p.vx = u2[2]
                p.vx = u2[3]

    def move(self):
        self.x+=self.vx
        self.y+=self.vy

    def update_p(self, collision_array):
        self.wall()
        self.collision(collision_array)
        self.move()