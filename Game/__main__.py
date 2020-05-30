from BreakOutGame.classes import *
from BreakOutGame.globalVariables import *
from BreakOutGame.functions import *
from BreakOutGame.levelsPackage.levels import *

pygame.init()
pygame.display.set_caption("BreakOut Game IA")
pygame.mouse.set_visible(False)

background = Sprite('pictures/background.png', (0, 0))
game_name = draw_text("BreakOut Game IA", font_ARLRDBD, (255,255,255), 45)

menu_group = pygame.sprite.Group()
menu = Sprite('pictures/menu_home.png', (0 ,0))
menu.rect[0] = SCREEN_WIDTH/2 - menu.rect[2]/2
menu.rect[1] = SCREEN_HEIGHT/2 - menu.rect[3]/2 + 50
menu_group.add(menu)

items_menu = pygame.sprite.Group()
item_master = Sprite('pictures/item_menu.png', (0,0))
for i in range(4):
    item = Sprite('pictures/item_menu.png', (SCREEN_WIDTH/2 - item_master.rect[2]/2, i*60 + SCREEN_HEIGHT/2 - 50))
    items_menu.add(item)

item_menu_selected_group = pygame.sprite.Group()
item_menu_selected = Sprite('pictures/item_menu_selected.png', (0, 0))
item_menu_selected.rect[0] = SCREEN_WIDTH/2 - item_menu_selected.rect[2]/2 + 3
item_menu_selected_group.add(item_menu_selected)

menu_selected = 0
item_menu_selected.rect[1] = items_menu.sprites()[menu_selected].rect[1]
text_menu = [draw_text("PLAY", font_GOTHIC, (255,255,255), 25)[0], draw_text("DIFFICULTY", font_GOTHIC, (255,255,255), 25)[0], draw_text("ABOUT", font_GOTHIC, (255,255,255), 25)[0], draw_text("EXIT", font_GOTHIC, (255,255,255), 25)[0]]

pygame.key.start_text_input()

while True:

    FPS.tick(30)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()

            if event.key == K_DOWN:
                if menu_selected >= 3:
                    menu_selected = 0
                else:
                   menu_selected += 1

            if event.key == K_UP:
                if menu_selected <= 0:
                    menu_selected = 3
                else:
                    menu_selected -= 1

            if event.key == K_RETURN or event.key == K_KP_ENTER:
                if menu_selected == 0:
                    levels_module()

                if menu_selected == 3:
                    pygame.quit()

    item_menu_selected.rect[1] = items_menu.sprites()[menu_selected].rect[1]

    screen.blit(background.image, (0, 0))
    screen.blit(game_name[0], (SCREEN_WIDTH/2 - game_name[1]/2, menu.rect[1] - 70))

    menu_group.draw(screen)
    items_menu.draw(screen)
    item_menu_selected_group.draw(screen)

    for i in range(4):
        screen.blit(text_menu[i], (SCREEN_WIDTH/2 - pygame.Surface.get_size(text_menu[i])[0]/2, i*60 + SCREEN_HEIGHT/2 - 50))