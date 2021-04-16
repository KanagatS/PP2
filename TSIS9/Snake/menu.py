import pygame

pygame.init()

pygame.display.set_caption('MENU BETA')

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_GREEN = (153, 255, 153)
YELLOW = (255, 255, 0)

FPS = 30

BG = pygame.image.load('background.jpg')
BG = pygame.transform.scale(BG, (800, 800))

FONT = pygame.font.SysFont('Arial', 50)
FONT_small = pygame.font.SysFont('Arial', 35)
FONT_verysmall = pygame.font.SysFont('Arial', 22)

# EASYLEVEL = pygame.image.load('easy.jpg')
# MEDUIMLEVEL = pygame.image.load('medium.jpg')
# HARDLEVEL = pygame.image.load('hard.jpg')


def draw_menu():
    WIN.blit(BG, (0, 0))
    CHOOSE_MODE = FONT.render('CHOOSE GAME MODE', True, WHITE)
    SINGLEPLAYER = FONT_small.render('SINGLE PLAYER', True, WHITE)
    MULTIPLAYER = FONT_small.render('MULTI PLAYER', True, WHITE)
    CHOOSE_LEVEL = FONT.render('CHOOSE LEVEL', True, WHITE)

    WIN.blit(CHOOSE_MODE, (130, 130))
    WIN.blit(SINGLEPLAYER, (80, 260))
    WIN.blit(MULTIPLAYER, (480, 260))
    pygame.draw.rect(WIN, YELLOW, [60, 250, 310, 60], 3)
    pygame.draw.rect(WIN, YELLOW, [450, 250, 310, 60], 3)

    WIN.blit(CHOOSE_LEVEL, (210, 400))
    pygame.draw.rect(WIN, YELLOW, [60, 500, 175, 175], 3)
    pygame.draw.rect(WIN, YELLOW, [313, 500, 175, 175], 3)
    pygame.draw.rect(WIN, YELLOW, [565, 500, 175, 175], 3)

    EASY = FONT_small.render('EASY', True, WHITE)
    EASY_text = FONT_verysmall.render('Free Field, Speed - 4', True, WHITE)

    MEDIUM = FONT_small.render('MEDIUM', True, WHITE)
    MEDIUM_text = FONT_verysmall.render('Borders, Speed - 7', True, WHITE)

    HARD = FONT_small.render('HARD', True, WHITE)
    HARD_text = FONT_verysmall.render('Labirint, Speed - 10', True, WHITE)

    WIN.blit(EASY, (100, 685))
    WIN.blit(EASY_text, (45, 730))

    WIN.blit(MEDIUM, (330, 685))
    WIN.blit(MEDIUM_text, (308, 730))

    WIN.blit(HARD, (605, 685))
    WIN.blit(HARD_text, (560, 730))


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        draw_menu()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
