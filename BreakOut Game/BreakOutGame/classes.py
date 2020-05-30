import pygame
from pygame.locals import *
from BreakOutGame.globalVariables import *

class Sprite(pygame.sprite.Sprite):
    def __init__(self, diretory, pos = []):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(diretory)
        self.rect = self.image.get_rect()
        self.rect[0] = pos[0]
        self.rect[1] = pos[1]

    def update(self):
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self, diretory, ypos, lifes):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(diretory).convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = (SCREEN_WIDTH / 2) - (self.rect[2] / 2)
        self.rect[1] = ypos
        self.rect[2] = self.rect[2]
        self.lifes = lifes

    def update(self):
        pass

    def moveLeft(self):
        if self.rect[0] >= VELOCITY_PLAYERPERSON:
            self.rect[0] -= VELOCITY_PLAYERPERSON
        elif self.rect[0] - VELOCITY_PLAYERPERSON < 0:
            self.rect[0] = 0

    def moveRight(self):
        if self.rect[0]+self.rect[2] + VELOCITY_PLAYERPERSON <= SCREEN_WIDTH:
            self.rect[0] += VELOCITY_PLAYERPERSON
        elif self.rect[0]+self.rect[2] + VELOCITY_PLAYERPERSON > SCREEN_WIDTH:
            self.rect[0] = SCREEN_WIDTH - self.rect[2]

class Ball(pygame.sprite.Sprite):
    def __init__(self, diretory, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(diretory).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = ypos
    
    def update(self):
        pass

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, diretory, xpos, ypos):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(diretory).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = ypos

    def update(self):
        pass