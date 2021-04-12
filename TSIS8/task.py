import pygame
import random
import time

pygame.init()

pygame.display.set_caption('TSIS 8')

WIDTH, HEIGHT = 400, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

FONT = pygame.font.Font(None, 80)

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

FPS = 60
SPEED = 10
SCORE = 0

PLAYER = pygame.image.load('player.png')
PLAYER = pygame.transform.scale(PLAYER, (100, 50))
PLAYER = pygame.transform.rotate(PLAYER, 270)

ENEMY = pygame.image.load('enemy.png')
ENEMY = pygame.transform.scale(ENEMY, (100, 50))
ENEMY = pygame.transform.rotate(ENEMY, 90)

COIN = pygame.image.load('coin.png')
COIN = pygame.transform.scale(COIN, (20, 20))

BACKGROUND = pygame.image.load('road.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND, (HEIGHT, WIDTH))
BACKGROUND = pygame.transform.rotate(BACKGROUND, 90)

GAMEOVER_TEXT = FONT.render('WASTED', True, RED)


class Coins(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = COIN
        self.surf = pygame.Surface((20, 20))
        self.rect = self.surf.get_rect(
            center=(random.randint(60, WIDTH - 55), 5))

    def move(self):
        global SCORE
        self.rect.move_ip(0, 5)

        if self.rect.top > HEIGHT:
            self.rect.top = 5
            self.rect.center = (random.randint(60, WIDTH - 55), 5)

        if pygame.sprite.spritecollideany(P1, coin):
            SCORE += 1
            self.rect.top = HEIGHT + 10


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ENEMY
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(
            center=(random.randint(60, WIDTH - 55), 5))

    def move(self):
        self.rect.move_ip(0, 10)  # RANDOM SPEED OF ENEMY
        if (self.rect.top > HEIGHT):
            self.rect.top = 5
            self.rect.center = (random.randint(60, WIDTH - 55), 5)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PLAYER
        self.surf = pygame.Surface((50, 100))
        self.rect = self.surf.get_rect(center=(150, 500))

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top > 5:
            self.rect.move_ip(0, -SPEED)
        if pressed[pygame.K_DOWN] and self.rect.top < 495:
            self.rect.move_ip(0, SPEED)
        if pressed[pygame.K_LEFT] and self.rect.left > 60:
            self.rect.move_ip(-SPEED, 0)
        if pressed[pygame.K_RIGHT] and self.rect.right < WIDTH - 55:
            self.rect.move_ip(SPEED, 0)


P1, E1, C1 = Player(), Enemy(), Coins()

enemies = pygame.sprite.Group()
enemies.add(E1)

coin = pygame.sprite.Group()
coin.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)


def draw_window():
    WIN.blit(BACKGROUND, (0, 0))

    SCORE_TEXT = FONT.render(str(SCORE), True, YELLOW)
    WIN.blit(SCORE_TEXT, (20, 20))

    for i in all_sprites:
        WIN.blit(i.image, i.rect)
        i.move()

    if pygame.sprite.spritecollideany(P1, enemies):
        WIN.fill(GREY)
        WIN.blit(GAMEOVER_TEXT, (75, 250))
        pygame.draw.rect(WIN, BLACK, (50, 225, 300, 100), 6)

        pygame.display.update()

        time.sleep(1)

        pygame.quit()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                run = False

        draw_window()

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
