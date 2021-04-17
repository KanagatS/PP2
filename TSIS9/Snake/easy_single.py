import pygame
import random
import time

pygame.init()

pygame.display.set_caption('SNAKE')

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_GREEN = (153, 255, 153)
YELLOW = (255, 255, 0)

FRUITS = []
for i in range(3):
    FRUITS.append(pygame.image.load(f'Pictures/fruit_{i}.png'))

FONT = pygame.font.SysFont('Courier', 35)
FONT_2 = pygame.font.SysFont('Arial', 48)

FPS = 60
VEL = 5


class Food():
    def __init__(self):
        self.x = random.randint(0, WIDTH - 35)
        self.y = random.randint(0, HEIGHT - 35)
        self.image = random.choice(FRUITS)
        self.image = pygame.transform.scale(self.image, (35, 35))

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


class Snake():
    def __init__(self):
        self.size = 2
        self.radius = 10
        self.dx = VEL
        self.dy = 0
        self.elements = [[100, 100], [120, 100]]
        self.score = 0
        self.is_add = False

    def draw(self):
        for element in self.elements:
            pygame.draw.circle(WIN, BLACK, element, self.radius)

    def move(self):
        if self.is_add:
            self.addSnake()
        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i-1][0]
            self.elements[i][1] = self.elements[i-1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

    def addSnake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False


def save_game():
    pass


def game_over():
    WIN.fill(RED)

    GAMEOVER_TEXT = FONT_2.render('GAME OVER!', True, BLACK)
    SCORE_TEXT = FONT_2.render('Your score: ' + str(snake.score), True, BLACK)

    WIN.blit(GAMEOVER_TEXT, (240, 250))
    WIN.blit(SCORE_TEXT, (240, 350))

    pygame.display.update()
    time.sleep(5)

    save_game()

    pygame.quit()


def collision_with_tail():
    pass


def collision_with_food():
    if (food.x in range(snake.elements[0][0] - 35, snake.elements[0][0]) and
            (food.y in range(snake.elements[0][1] - 35, snake.elements[0][1]))):
        snake.is_add = True
        food.x = random.randint(0, WIDTH - 35)
        food.y = random.randint(0, HEIGHT - 35)


def show_score(x, y, score):
    score_text = FONT.render('Score: ' + str(score), True, BLACK)
    WIN.blit(score_text, (x, y))


def draw_window():
    WIN.fill(LIGHT_GREEN)

    movement()

    snake.draw()
    snake.move()

    collision_with_food()

    food.draw()

    show_score(40, 35, snake.score)


def movement():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT]:
        snake.dx = VEL
        snake.dy = 0
    elif pressed[pygame.K_LEFT]:
        snake.dx = -VEL
        snake.dy = 0
    elif pressed[pygame.K_UP]:
        snake.dx = 0
        snake.dy = -VEL
    elif pressed[pygame.K_DOWN]:
        snake.dx = 0
        snake.dy = VEL


snake = Snake()
food = Food()


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

        if collision_with_tail():
            game_over()
        draw_window()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
