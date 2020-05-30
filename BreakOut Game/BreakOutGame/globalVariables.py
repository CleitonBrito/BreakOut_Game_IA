import pygame
from pygame.locals import *

FPS = pygame.time.Clock()

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)

VELOCITY_PLAYER01 = 20
VELOCITY_PLAYERPERSON = 50

font_GOTHIC = "GOTHIC.TTF"
font_ARLRDBD = "ARLRDBD.TTF"