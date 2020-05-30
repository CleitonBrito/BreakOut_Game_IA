import pygame
from pygame.locals import *
from BreakOutGame.classes import *

def draw_text(text, font, color, size):
    my_font = pygame.font.Font('fonts/%s' %font, size)
    width_text_score = pygame.font.Font.size(my_font, text)[0]
    text = my_font.render(text, True, color)
    return text, width_text_score

def lifes_Player01(lifes):
    lifes_Player01_group = pygame.sprite.Group()
    lifes_Player01_master = Sprite('pictures/heart.png', (SCREEN_WIDTH - 165, 0))
    lifes_Player01_master.rect[0] -= lifes_Player01_master.rect[2] + 10
    for i in range(lifes):
        lifes_Player01 = Sprite('pictures/heart.png', (lifes_Player01_master.rect[0], 15))
        lifes_Player01_master.rect[0] = lifes_Player01_master.rect[0]-lifes_Player01_master.rect[2]-5
        lifes_Player01_group.add(lifes_Player01)

    return lifes_Player01_group

def lifes_PlayerPerson(posx, lifes):
    lifes_PlayerPerson_group = pygame.sprite.Group()
    lifes_PlayerPerson_master = Sprite('pictures/heart.png', (posx, 0))
    lifes_PlayerPerson_master.rect[0] += 10
    for i in range(lifes):
        lifes_PlayerPerson = Sprite('pictures/heart.png', (lifes_PlayerPerson_master.rect[0], 15))
        lifes_PlayerPerson_master.rect[0] = lifes_PlayerPerson_master.rect[0]+lifes_PlayerPerson_master.rect[2]+5
        lifes_PlayerPerson_group.add(lifes_PlayerPerson)

    return lifes_PlayerPerson_group

def calculate_interval_between(screenWidth, itemWidth, quantityItems):
    result_interval = round((screenWidth - (quantityItems * itemWidth))/(quantityItems+1))
    if result_interval > 0:
        return result_interval
    else:
        return 0

def calculate_position(interval, itemWidth, quantityItems):
    positions = []
    if interval > 0:
        for i in range(round(quantityItems)):
            result = interval + (i * (itemWidth + interval))
            positions.append(result)
    else:
        for i in range(round(quantityItems)):
            positions.append(0)

    return positions

def removeLife(GroupPlayer, GroupLifes):
    SpritesPlayer = GroupPlayer.sprites()
    SpritesLifes = GroupLifes.sprites()
    if SpritesPlayer[0].lifes > 0:
        for i in range(len(GroupPlayer)):
            SpritesPlayer[i].lifes -= 1

        life_remove = SpritesLifes[SpritesPlayer[0].lifes]
        GroupLifes.remove(life_remove)