import pygame
import math
import sys

pygame.init()

pygame.display.set_caption('TSIS 7')

WIDTH, HEIGHT = 1000, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.Font(None, 36)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

PI = 3.14


def draw_numbers():
    numbers = [1.00, 0.75, 0.50, 0.25, 0.00, -0.25, -0.50, -0.75, -1.00]
    FONT = pygame.font.Font(None, 24)
    WIN.blit(FONT.render('-3', 1, BLACK), (85, 380))
    WIN.blit(FONT.render('-2', 1, BLACK), (167, 380))
    WIN.blit(FONT.render('-1', 1, BLACK), (265, 380))
    FONT = pygame.font.Font(None, 36)
    WIN.blit(FONT.render('1.00', 1, BLACK), (915, 36))
    WIN.blit(FONT.render('0.75', 1, BLACK), (915, 105))
    WIN.blit(FONT.render('0.50', 1, BLACK), (915, 174))
    WIN.blit(FONT.render('0.25', 1, BLACK), (915, 243))
    WIN.blit(FONT.render('0.00', 1, BLACK), (915, 312))
    WIN.blit(FONT.render('-0.25', 1, BLACK), (915, 381))
    WIN.blit(FONT.render('-0.50', 1, BLACK), (915, 450))
    WIN.blit(FONT.render('-0.75', 1, BLACK), (915, 519))
    WIN.blit(FONT.render('-1.00', 1, BLACK), (915, 588))

    # for y in range(36, 588 + 1, 69):
    #     for i in range(len(numbers)):
    #         WIN.blit(FONT.render(f'{str(numbers[i])}', 1, BLACK), (915, y))


def draw_radians():
    WIN.blit(FONT.render('X', 1, BLACK), (465, 630))


def draw_text():
    SIN_text = FONT.render('sin(x)', 1, BLACK)
    WIN.blit(SIN_text, (570, 90))
    pygame.draw.line(WIN, RED, (640, 100), (700, 100), 3)
    
    COS_text = FONT.render('cos(x)', 1, BLACK)
    WIN.blit(COS_text, (570, 120))
    pygame.draw.line(WIN, BLUE, (645, 130), (700, 130), 3)


def draw_cos():
    for x in range(80, 870 + 1):
        cos1 = 244 * math.cos((x - 80) / 132 * PI)
        cos2 = 244 * math.cos((x - 77) / 132 * PI)
        pygame.draw.aalines(WIN, BLUE, False, [(x - 1, cos1 + 325), (x, cos2 + 325)])


def draw_sin():
    for x in range(80, 870 + 1):
        sin1 = 244 * math.sin((x - 80) / 132 * PI)
        sin2 = 244 * math.sin((x - 77) / 132 * PI)
        pygame.draw.aalines(WIN, RED, False, [(x - 1, sin1 + 325), (x, sin2 + 325)])


def draw_grid_y():
    pygame.draw.line(WIN, BLACK, (80, 50), (80, 600), 2)
    pygame.draw.line(WIN, BLACK, (870, 50), (870, 600), 2)

    for y in range(50, 600 + 1, 69):
        pygame.draw.line(WIN, BLACK, (50, y), (900, y), 2)

    for y in range(80, 600 + 1 - 30, 34):
        pygame.draw.line(WIN, BLACK, (50, y), (75, y), 2)
        pygame.draw.line(WIN, BLACK, (875, y), (900, y), 2)

    for y in range(80, 600 + 1 - 30, 17):
        pygame.draw.line(WIN, BLACK, (50, y), (68, y), 2)
        pygame.draw.line(WIN, BLACK, (882, y), (900, y), 2)


def draw_grid_x():
    pygame.draw.line(WIN, BLACK, (50, 80), (900, 80), 2)
    pygame.draw.line(WIN, BLACK, (50, 570), (900, 570), 2)

    for x in range(50, 900 - 10, 140):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 600), 2)

    for x in range(80, 900 + 1 - 30, 70):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 75), 2)
        pygame.draw.line(WIN, BLACK, (x, 600), (x, 575), 2)

    for x in range(80, 900 + 1 - 30, 35):
        pygame.draw.line(WIN, BLACK, (x, 50), (x, 68), 2)
        pygame.draw.line(WIN, BLACK, (x, 600), (x, 582), 2)


def draw_lines():
    pygame.draw.line(WIN, BLACK, (50, 325), (900, 325), 3)
    pygame.draw.line(WIN, BLACK, (472, 50), (472, 600), 3)


def draw_borders():
    pygame.draw.rect(WIN, BLACK, (50, 50, 850, 550), 3)


def draw_window():
    WIN.fill(WHITE)
    draw_borders()
    draw_lines()
    draw_grid_x()
    draw_grid_y()
    draw_sin()
    draw_cos()
    draw_text()
    draw_radians()
    draw_numbers()
    pygame.display.update()


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()


if __name__ == '__main__':
    main()
