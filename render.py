import sys
import pygame
import constants

pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0


scale = 6
screen = pygame.display.set_mode(size)

bounds_offset_x = 5 * scale
bounds_offset_y = 5 * scale

def draw_bounds(color):
    pygame.draw.rect(screen,color,[0,0,constants.WORLD_SIZE*scale,constants.WORLD_SIZE*scale],5)

    #bounds_offset = 5 + 1 * 10 * scale

def draw_particles(particles : list, color):

    for p in particles:
        pygame.draw.circle(screen,color, (p.x*scale*10 + bounds_offset_x, p.y*scale*10 + bounds_offset_y), 1*scale )

from world import World
w = World(10,100)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    screen.fill(black)

    draw_bounds(red)
    draw_particles(w.particles,white)

    pygame.display.flip()