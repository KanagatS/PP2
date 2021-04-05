import pygame
import math
import sys

pygame.init()

pygame.display.set_caption('TSIS 7')

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.14


def draw_text():
    FONT = pygame.font.Font(None, 36)
    SIN_text = FONT.render('sin x', 1, BLACK)
    COS_text = FONT.render('cos x', 1, BLACK)
    WIN.blit(SIN_text, (550, 100))
    WIN.blit(COS_text, (550, 120))


def draw_cos():
    for x in range(80, 870 + 1):  # COS
        cos1 = 240 * math.cos((x - 80) / 80 * 3.14)
        cos2 = 240 * math.cos((x - 79) / 80 * 3.14)
        pygame.draw.aalines(WIN, BLUE, False, [(x, cos1 + 325), ((x + 1), cos2 + 325)])


def draw_sin():
    for x in range(80, 870 + 1):  # SIN
        sin1 = 240 * math.sin((x - 80) / 80 * 3.14)
        sin2 = 240 * math.sin((x - 79) / 80 * 3.14)
        pygame.draw.aalines(WIN, RED, False, [(x, sin1 + 325), ((x + 1), sin2 + 325)])


def draw_grid():
    pygame.draw.line(WIN, BLACK, (50, 80), (900, 80))  # thin line X
    pygame.draw.line(WIN, BLACK, (50, 570), (900, 570))  # thin line X

    pygame.draw.line(WIN, BLACK, (80, 50), (80, 600))  # thin line Y
    pygame.draw.line(WIN, BLACK, (870, 50), (870, 600))  # thin line Y

    for x in range(50, 900 + 1, 140):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 600))

    for x in range(50, 900 + 1, 70):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 75))
        pygame.draw.line(WIN, BLACK, (x, 600), (x, 575))

    for x in range(50, 900 + 1, 35):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 68))
        pygame.draw.line(WIN, BLACK, (x, 600), (x, 582))


def draw_lines():
    pygame.draw.line(WIN, BLACK, (50, 325), (900, 325), 3)  # x
    pygame.draw.line(WIN, BLACK, (475, 50), (475, 600), 3)  # y


def draw_borders():
    pygame.draw.rect(WIN, BLACK, (50, 50, 850, 550), 3)


def draw_window():
    WIN.fill(WHITE)
    draw_borders()
    draw_lines()
    draw_grid()
    draw_sin()
    draw_cos()
    draw_text()
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.K_ESCAPE:
                sys.exit()

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
