import pygame
from pygame.locals import *
from BreakOutGame.classes import *
from BreakOutGame.functions import *
from BreakOutGame.globalVariables import *
from BreakOutGame.levelsPackage import levels

areaUpSide_group = pygame.sprite.Group()
areaUpSide = Sprite('pictures/up_side.png', (0, 0))
areaUpSide_group.add(areaUpSide)

count_lifes_player = 3

player01_group = pygame.sprite.Group()
player01 = [Player('pictures/player01_size0.png', 0, count_lifes_player), Player('pictures/player01_size1.png', 0, count_lifes_player), Player('pictures/player01_size2.png', 0, count_lifes_player), Player('pictures/player01_size3.png', 0, count_lifes_player)]
for i in range(4):
    player01[i].rect[0] = SCREEN_WIDTH/2 - player01[i].rect[2]/2
    player01[i].rect[1] = areaUpSide.rect[3] + 20
player01_group.add(player01)

playerPerson_group = pygame.sprite.Group()
playerPerson = [Player('pictures/playerPerson_size0.png', 0, count_lifes_player), Player('pictures/playerPerson_size1.png', 0, count_lifes_player), Player('pictures/playerPerson_size2.png', 0, count_lifes_player), Player('pictures/playerPerson_size3.png', 0, count_lifes_player), ]
for i in range(4):
    playerPerson[i].rect[0] = SCREEN_WIDTH/2 - playerPerson[i].rect[2]/2
    playerPerson[i].rect[1] = SCREEN_HEIGHT-playerPerson[i].rect[3] - 20
playerPerson_group.add(playerPerson)

def level01_module():
    runing = True
    currentPlayerSize = 3
    marginEdge = 45
    pygame.display.flip()

    label_namePlayer01 = draw_text("Player01", font_GOTHIC, (255,255, 255), 30)
    label_namePlayerPerson = draw_text("Brito", font_GOTHIC, (255,255,255), 30)
    label_level = draw_text("Level 1", font_ARLRDBD, (255,255,255), 30)

    lifes_Player01_group = lifes_Player01(count_lifes_player)
    lifes_PlayerPerson_group = lifes_PlayerPerson(label_namePlayerPerson[1]+marginEdge, count_lifes_player)

    SpritesPlayerPerson = playerPerson_group.sprites()

    while runing:
        FPS.tick(120)
        pygame.display.update()

        currentPlayerPerson = SpritesPlayerPerson[currentPlayerSize]

        if pygame.key.get_pressed()[pygame.K_LEFT]:
            for i in range(len(playerPerson_group)):
                SpritesPlayerPerson[i].moveLeft()

        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            for i in range(len(playerPerson_group)):
                SpritesPlayerPerson[i].moveRight()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()

                if event.key == K_BACKSPACE:
                    runing = False
                    levels.levels_module()

                if event.key == K_UP:
                    removeLife(playerPerson_group, lifes_PlayerPerson_group)
                    if currentPlayerSize < 3:
                        currentPlayerSize += 1

                if event.key == K_DOWN:
                    if currentPlayerSize > 0:
                        currentPlayerSize -= 1

        background = Sprite('pictures/background.png', (0, 0))
        screen.blit(background.image, (0,0))

        areaUpSide_group.update()
        player01_group.update()
        playerPerson_group.update()
        lifes_Player01_group.update()
        lifes_PlayerPerson_group.update()

        areaUpSide_group.draw(screen)
        player01_group.draw(screen)
        lifes_Player01_group.draw(screen)
        lifes_PlayerPerson_group.draw(screen)
        
        screen.blit(label_namePlayer01[0], (SCREEN_WIDTH-label_namePlayer01[1]-marginEdge, 5))
        screen.blit(label_namePlayerPerson[0], (marginEdge, 5))
        screen.blit(label_level[0], (SCREEN_WIDTH/2-label_level[1]/2, 5))

        screen.blit(currentPlayerPerson.image, (currentPlayerPerson.rect[0], currentPlayerPerson.rect[1]))
