import pygame
from pygame.locals import *
from BreakOutGame.classes import *
from BreakOutGame.globalVariables import *
from BreakOutGame.functions import *
from BreakOutGame.levelsPackage import level01

levels_group = pygame.sprite.Group()
levels = Sprite('pictures/levels.png', (0, 0))
levels.rect[0] = SCREEN_WIDTH/2 - levels.rect[2]/2
levels.rect[1] = SCREEN_HEIGHT/2 - levels.rect[3]/2
levels_group.add(levels)

level_circle_group = pygame.sprite.Group()
level_circle_master = Sprite('pictures/level_circle.png', (0, 0))
quantity_items = 10
for i in range(round(quantity_items/2)):
    level_circle = Sprite('pictures/level_circle.png', (levels.rect[0], levels.rect[1] + 130))
    level_circle_group.add(level_circle)

for i in range(round(quantity_items/2)):
    level_circle = Sprite('pictures/level_circle.png', (levels.rect[0], levels.rect[1] + 300))
    level_circle_group.add(level_circle)

interval = calculate_interval_between(levels.rect[2], level_circle_master.rect[2], quantity_items/2)
position_levels_circe = calculate_position(interval, level_circle_master.rect[2], quantity_items/2)
sprites_circles = level_circle_group.sprites()

j = 0
for i in range(len(sprites_circles)):
    if j > len(sprites_circles)/2-1:
        j = 0
    sprites_circles[i].rect[0] = position_levels_circe[j] + levels.rect[0]
    j += 1

level_selected_group = pygame.sprite.Group()
level_selected = Sprite('pictures/level_selected.png', (0, 0))
level_selected_group.add(level_selected)

level_blocked_group = pygame.sprite.Group()
for i in range(quantity_items-1):
    level_blocked = Sprite('pictures/level_blocked.png', (0, 0))
    level_blocked_group.add(level_blocked)
sprite_level_blocked = level_blocked_group.sprites()

levels_quantity = 11

def levels_module():

    text_levels = []
    for i in range(levels_quantity):
        text = draw_text(str(i+1), font_ARLRDBD, (255,255,255), 60)[0]
        text_levels.append(text)

    lvl_selected = 0
    lvl_unlocked = 0
    level_selected.rect[0] = sprites_circles[0].rect[0]
    level_selected.rect[1] = sprites_circles[0].rect[1]

    running = True

    while running:

        FPS.tick(30)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()

                if event.key == K_BACKSPACE:
                    running = False

                if event.key == K_LEFT:
                    if lvl_selected > 0:
                        lvl_selected -= 1
                    else:
                        lvl_selected = lvl_unlocked

                if event.key == K_RIGHT:
                    if lvl_selected < lvl_unlocked:
                        lvl_selected += 1
                    else:
                        lvl_selected = 0

                if event.key == K_RETURN or event.key == K_KP_ENTER:
                    if lvl_selected == 0:
                        running = False
                        level01.level01_module()

        background = Sprite('pictures/background.png', (0, 0))
        screen.blit(background.image, (0,0))

        level_selected.rect[0] = sprites_circles[lvl_selected].rect[0]
        level_selected.rect[1] = sprites_circles[lvl_selected].rect[1]

        levels_group.draw(screen)
        level_circle_group.draw(screen)
        level_selected_group.draw(screen)

        for i in range(levels_quantity-1):
            Number_centerX = sprites_circles[i].rect[0]+(sprites_circles[i].rect[2]/2)-(pygame.Surface.get_size(text_levels[i])[0]/2)
            Number_centerY = sprites_circles[i].rect[1]+(sprites_circles[i].rect[3]/2)-(pygame.Surface.get_size(text_levels[i])[1]/2)
            blocked_centerX = sprites_circles[i].rect[0]+(sprite_level_blocked[i-1].rect[2]/2)
            blocked_centerY = sprites_circles[i].rect[1]+(sprite_level_blocked[i-1].rect[3]/2)

            screen.blit(text_levels[i], (Number_centerX, Number_centerY))
            if i > lvl_unlocked:
                screen.blit(sprite_level_blocked[i-1].image, (blocked_centerX, blocked_centerY))