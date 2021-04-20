import pygame

pygame.init()

pygame.display.set_caption('Paint Clone for TSIS9')

WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.SysFont('Arial', 30)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


def save_picture():
    pygame.image.save(WIN, 'picture.jpg')


def draw_line(screen, start, end, width, color):
    x1, x2 = start[0], end[0]
    y1, y2 = start[1], end[1]

    dx, dy = abs(x1 - x2), abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


def draw_menu(open, color, radius):
    pygame.draw.rect(WIN, BLACK, [0, 0, WIDTH, HEIGHT], 3)  # BORDER

    if open:
        pygame.draw.rect(WIN, BLACK, [1440, 0, 160, 408], 3)

        WIN.blit(FONT.render('1 - ', True, BLACK), (1450, 5))
        WIN.blit(FONT.render('2 - ', True, BLACK), (1450, 45))
        WIN.blit(FONT.render('3 - ', True, BLACK), (1450, 85))
        WIN.blit(FONT.render('4 - ', True, BLACK), (1450, 125))
        WIN.blit(FONT.render('5 - ', True, BLACK), (1450, 165))
        WIN.blit(FONT.render('E - Eraser', True, BLACK), (1450, 205))
        WIN.blit(FONT.render('R - ', True, BLACK), (1450, 245))
        WIN.blit(FONT.render('C - ', True, BLACK), (1450, 285))
        WIN.blit(FONT.render('- color ', True, BLACK), (1500, 325))

        pygame.draw.rect(WIN, BLACK, [1500, 5, 50, 30])
        pygame.draw.rect(WIN, RED, [1500, 45, 50, 30])
        pygame.draw.rect(WIN, GREEN, [1500, 85, 50, 30])
        pygame.draw.rect(WIN, BLUE, [1500, 125, 50, 30])
        pygame.draw.rect(WIN, YELLOW, [1500, 165, 50, 30])
        pygame.draw.rect(WIN, BLACK, [1500, 245, 50, 30], 3)
        pygame.draw.circle(WIN, BLACK, (1520, 304), 15, 3)

        pygame.draw.rect(WIN, BLACK, [1448, 323, 43, 43], 3)
        pygame.draw.rect(WIN, color, [1450, 325, 40, 40])

        WIN.blit(FONT.render('R = ' + str(radius), True, BLACK), (1450, 370))


def main():
    run, draw_on = True, False
    open = False
    last_pos = (0, 0)
    radius = 10
    color = BLACK

    WIN.fill(WHITE)

    while run:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    save_picture()
                elif event.key == pygame.K_o:  # HINT
                    open = not open

                elif event.key == pygame.K_q:  # CLEAR
                    WIN.fill(WHITE)

                elif event.key == pygame.K_e:  # ERASER
                    color = WHITE
                elif event.key == pygame.K_1:
                    color = BLACK
                elif event.key == pygame.K_2:
                    color = RED
                elif event.key == pygame.K_3:
                    color = GREEN
                elif event.key == pygame.K_4:
                    color = BLUE
                elif event.key == pygame.K_5:
                    color = YELLOW

                elif event.key == pygame.K_UP and radius < 30:
                    radius += 1
                elif event.key == pygame.K_DOWN and radius >= 3:
                    radius -= 1

                elif event.key == pygame.K_r:
                    pygame.draw.rect(WIN, color, [mx, my, radius + 200, radius + 100], 4)
                elif event.key == pygame.K_c:
                    pygame.draw.circle(WIN, color, (mx, my), radius + 50, 4)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.circle(WIN, color, event.pos, radius)
                draw_on = True

            elif event.type == pygame.MOUSEBUTTONUP:
                draw_on = False

            elif event.type == pygame.MOUSEMOTION:
                if draw_on:
                    draw_line(WIN, last_pos, event.pos, radius, color)
                last_pos = event.pos

        draw_menu(open, color, radius)
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
