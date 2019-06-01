import sys
import pygame
import constants
import random
import math

pygame.init()

size = width, height = 1000, 600
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0


scale = 6
screen = pygame.display.set_mode(size)

bounds_offset_x = 5 * scale
bounds_offset_y = 5 * scale

def draw_bounds(color):
    pygame.draw.rect(screen,color,[0,0,constants.WORLD_SIZE,constants.WORLD_SIZE],2)

    #bounds_offset = 5 + 1 * 10 * scale

def draw_particles(particles : list, color):

    for p in particles:
        pygame.draw.circle(screen, color,(int(p.x), int(p.y)), 5)


from world import World

w = World(500,500)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    screen.fill(black)

    draw_bounds(red)
    draw_particles(w.particles,white)
    w.update()
    pygame.display.flip()

