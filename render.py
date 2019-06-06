import sys
import pygame
import constants
import random
import math
import plotly.plotly
import plotly.graph_objs as go

pygame.init()

size = width, height = 1200, 900
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

w = World(constants.WORLD_SIZE)
entropy = []
time = []
chart = []

for i in range(constants.TIME_RANGE):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    screen.fill(black)

    draw_bounds(red)
    draw_particles(w.particles,white)
    w.update()
    entropy.append(w.entropy())
    time.append(i)
    pygame.display.flip()

chart.append(go.Scatter(x = time,y = entropy,mode = 'lines', name="Entropy"))
plotly.offline.plot(chart,filename="entropy.html")

sys.exit()