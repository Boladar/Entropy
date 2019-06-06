import math
import random

PARTICLE_MASS = 1
PARTICLE_RADIUS = 5
TIME_RANGE = 100

WORLD_SIZE = 800
NUMBER_OF_PARTICLES = int(math.sqrt(WORLD_SIZE)*10)


W = 100
#MAX_SPEED = int(W / (2 * NUMBER_OF_PARTICLES))
MAX_SPEED = 2000
TIME_STEP = 1/(2*W)
