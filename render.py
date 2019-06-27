import sys
import pygame
from world import World
import constants
import random
import math
import time
import plotly.plotly
import plotly.graph_objs as go

def text_tmp(e,i):
    text2 = font.render('{0:.2f}'.format(e), True, white)
    text2Rect = text2.get_rect()
    text2Rect.center = (constants.WORLD_SIZE + 100, 100)
    text4 = font.render('{0:.3f}'.format(i * constants.TIME_STEP), True, white)
    text4Rect = text4.get_rect()
    text4Rect.center = (constants.WORLD_SIZE + 100, 200)
    screen.blit(text2, text2Rect)
    screen.blit(text4, text4Rect)

def draw_bounds(color):
    pygame.draw.rect(screen, color, [0, 0, constants.WORLD_SIZE, constants.WORLD_SIZE], 2)

def draw_particles(particles : list, color):

    for p in particles:
        pygame.draw.circle(screen, color, (int(p.x), int(p.y)), constants.PARTICLE_RADIUS)

pygame.init()

size = width, height = 1200, 900
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

scale = 6
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Entropy")
font = pygame.font.Font('OpenSans-Bold.ttf', 32)
text1 = font.render('Entropy:', True, white)
text1Rect = text1.get_rect()
text1Rect.center = (constants.WORLD_SIZE+100,50)
text3 = font.render('Time:', True, white)
text3Rect = text3.get_rect()
text3Rect.center = (constants.WORLD_SIZE+100,150)

w = World(constants.WORLD_SIZE)
entropy = []
t = []
chart = []
w.all_states()

for i in range(constants.TIME_RANGE):
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    screen.fill(black)

    draw_bounds(red)
    screen.blit(text1, text1Rect)
    screen.blit(text3, text3Rect)
    draw_particles(w.particles, white)

    w.update()
    #print("\nPosition for time {}*{} : ".format(i,constants.TIME_STEP))
    #w.particle_positions()

    w.compute_state()

    e = w.entropy()
    if i > 50:
        entropy.append(e)
        t.append(i * constants.TIME_STEP)

    text_tmp(e, i)

    pygame.display.flip()

chart.append(go.Scatter(x = t, y = entropy, mode = 'lines', name="Entropy"))
plotly.offline.plot(chart, filename="entropy.html")

sys.exit()