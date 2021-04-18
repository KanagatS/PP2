import pygame
import os
import time

pygame.init()

pygame.display.set_caption('MENU')

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 160, 0)
YELLOW = (255, 255, 0)

BG = pygame.image.load('Pictures/bg.jpg')
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

SNAKE_HEAD = pygame.image.load('Pictures/snake_head.png')

ARROW = pygame.image.load('Pictures/arrow.png')
ARROW = pygame.transform.rotate(ARROW, 90)

FONT = pygame.font.SysFont('Arial', 50)
FONT_small = pygame.font.SysFont('Arial', 35)
FONT_verysmall = pygame.font.SysFont('Arial', 22)

EASYLEVEL = pygame.image.load('Levels/easy.png')
MEDIUMLEVEL = pygame.image.load('Levels/medium.png')
HARDLEVEL = pygame.image.load('Levels/hard.png')


def menu_functions(click, single, multi):
    easy_level_button = pygame.Rect(60, 500, 175, 175)
    medium_level_button = pygame.Rect(313, 500, 175, 175)
    hard_level_button = pygame.Rect(565, 500, 175, 175)

    easy, medium, hard = False, False, False

    mx, my = pygame.mouse.get_pos()

    if easy_level_button.collidepoint((mx, my)) and click:
        easy = True

    elif medium_level_button.collidepoint((mx, my)) and click:
        medium = True

    elif hard_level_button.collidepoint((mx, my)) and click:
        hard = True

    if single:
        if easy:
            time.sleep(0.5)
            os.system('easy_single.py')
        elif medium:
            time.sleep(0.5)
            os.system('medium_single.py')
        elif hard:
            time.sleep(0.5)
            os.system("hard_single.py")

    elif multi:
        if easy:
            time.sleep(0.5)
            os.system('easy_multi.py')
        elif medium:
            time.sleep(0.5)
            os.system("medium_multi.py")
        elif hard:
            time.sleep(0.5)
            os.system("hard_multi.py")


def draw_menu(single, multi):
    WIN.blit(BG, (0, 0))

    CHOOSE_MODE = FONT.render('CHOOSE GAME MODE', True, BLACK)
    SINGLEPLAYER = FONT_small.render('SINGLE PLAYER', True, BLACK)
    MULTIPLAYER = FONT_small.render('MULTI PLAYER', True, BLACK)
    CHOOSE_LEVEL = FONT.render('CHOOSE LEVEL', True, BLACK)

    WIN.blit(CHOOSE_MODE, (130, 130))
    WIN.blit(SINGLEPLAYER, (80, 260))
    WIN.blit(MULTIPLAYER, (480, 260))
    WIN.blit(CHOOSE_LEVEL, (210, 400))

    WIN.blit(SNAKE_HEAD, (60, 180))
    WIN.blit(SNAKE_HEAD, (670, 180))
    WIN.blit(SNAKE_HEAD, (700, 180))

    # Frames around the inscription
    pygame.draw.rect(WIN, YELLOW, [60, 250, 310, 60], 3)
    pygame.draw.rect(WIN, YELLOW, [450, 250, 310, 60], 3)

    pygame.draw.rect(WIN, GREEN, [60, 500, 175, 175], 8)
    pygame.draw.rect(WIN, YELLOW, [313, 500, 175, 175], 8)
    pygame.draw.rect(WIN, RED, [565, 500, 175, 175], 8)

    WIN.blit(EASYLEVEL, (60, 500))
    WIN.blit(MEDIUMLEVEL, (313, 500))
    WIN.blit(HARDLEVEL, (565, 500))

    EASY = FONT_small.render('EASY', True, WHITE)
    EASY_text = FONT_verysmall.render('Free Field, Speed - 5', True, WHITE)

    MEDIUM = FONT_small.render('MEDIUM', True, WHITE)
    MEDIUM_text = FONT_verysmall.render('Borders, Speed - 7', True, WHITE)

    HARD = FONT_small.render('HARD', True, WHITE)
    HARD_text = FONT_verysmall.render('Labirint, Speed - 8', True, WHITE)

    WIN.blit(EASY, (100, 685))
    WIN.blit(EASY_text, (45, 730))

    WIN.blit(MEDIUM, (330, 685))
    WIN.blit(MEDIUM_text, (308, 730))

    WIN.blit(HARD, (605, 685))
    WIN.blit(HARD_text, (560, 730))

    if single:
        WIN.blit(ARROW, (170, 320))
    elif multi:
        WIN.blit(ARROW, (565, 320))


def main():
    run = True
    click = False
    single, multi = False, False
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_1:
                    single = True
                    multi = False
                elif event.key == pygame.K_2:
                    multi = True
                    single = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click = True

        draw_menu(single, multi)
        menu_functions(click, single, multi)
        pygame.display.update()
        click = False

    pygame.quit()


if __name__ == '__main__':
    main()
