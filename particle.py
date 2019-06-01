import math
import constants
import random

class Particle:

    def __init__(self, x, y, vx, vy):

        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = 10

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
        #for p in collision_array:
            dx = -(self.x - p.x)
            dy = -(self.y - p.y)
            dist = math.sqrt(dx * dx + dy * dy)
            if dist <= 2 * constants.PARTICLE_RADIUS: #and self.x != p.x and self.y != p.y:
                overlap = 0.5 * (dist - 2 * constants.PARTICLE_RADIUS)
                self.x -= overlap * (self.x - p.x) / dist
                self.y -= overlap * (self.y - p.y) / dist
                p.x += overlap * (self.x - p.x) / dist
                p.x += overlap * (self.y - p.y) / dist

                V = math.sqrt((self.vx ** 2) + (self.vy ** 2))
                Vp = math.sqrt((p.vx ** 2) + (p.vy ** 2))
                if dx > 0:
                    if dy > 0:
                        angle = math.radians(math.degrees(math.atan(dy / dx)))
                        self.vx = -V * math.cos(angle)
                        self.vy = -V * math.sin(angle)
                        p.vx = Vp * math.cos(angle)
                        p.vy = Vp * math.sin(angle)
                    elif dy < 0:
                        angle = math.radians(math.degrees(math.atan(dy / dx)))
                        self.vx = -V * math.cos(angle)
                        self.vy = -V * math.sin(angle)
                        p.vx = Vp * math.cos(angle)
                        p.vy = Vp * math.sin(angle)
                elif dx < 0:
                    if dy > 0:
                        angle = math.radians(180 + math.degrees(math.atan(dy / dx)))
                        self.vx = -V * math.cos(angle)
                        self.vy = -V * math.sin(angle)
                        p.vx = Vp * math.cos(angle)
                        p.vy = Vp * math.sin(angle)
                    elif dy < 0:
                        angle = math.radians(-180 + math.degrees(math.atan(dy / dx)))
                        self.vx = -V * math.cos(angle)
                        self.vy = -V * math.sin(angle)
                        p.vx = Vp * math.cos(angle)
                        p.vy = Vp * math.sin(angle)
                elif dy == 0:
                    if dy > 0:
                        angle = math.radians(-90)
                    else:
                        angle = math.radians(90)
                    self.vx = V * math.cos(angle)
                    self.vy = V * math.sin(angle)
                    p.vx = -Vp * math.cos(angle)
                    p.vy = -Vp * math.sin(angle)
                elif dy == 0:
                    if dx < 0:
                        angle = 0
                    else:
                        angle = math.radians(180)
                    self.vx = V * math.cos(angle)
                    self.vy = V * math.sin(angle)
                    p.vx = -Vp * math.cos(angle)
                    p.vy = -Vp * math.sin(angle)

    def move(self):
        self.x+=self.vx
        self.y+=self.vy