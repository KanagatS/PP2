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

WALL = pygame.image.load('wall.png')
FRUITS = [pygame.image.load('apple.png'), pygame.image.load('sliva.png')]

FONT = pygame.font.SysFont('Courier', 35)

FPS = 60
VEL = 4


class Food():
    def __init__(self):
        self.x = random.randint(32, WIDTH - 32 - 35)
        self.y = random.randint(32, HEIGHT - 32 - 35)
        # self.image = pygame.image.load('apple.png')
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


def draw_menu():
    BG = pygame.image.load('background.jpg')
    BG = pygame.transform.scale(BG, (800, 800))

    FONT = pygame.font.SysFont('Arial', 50)
    FONT_small = pygame.font.SysFont('Arial', 35)
    FONT_verysmall = pygame.font.SysFont('Arial', 22)

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


def game_over():
    WIN.fill(RED)
    GAMEOVER_TEXT = FONT.render('GAME OVER!', True, BLACK)
    SCORE_TEXT1 = FONT.render(
        'Score of snake #1: ' + str(snake.score), True, BLACK)
    SCORE_TEXT2 = FONT.render(
        'Score of snake #2: ' + str(snake2.score), True, BLACK)
    LOOSER_TEXT = FONT.render('Loser is - ' + str(looser), True, BLACK)
    WIN.blit(GAMEOVER_TEXT, (200, 200))
    WIN.blit(SCORE_TEXT1, (200, 300))
    WIN.blit(SCORE_TEXT2, (200, 400))
    WIN.blit(LOOSER_TEXT, (200, 500))
    pygame.display.update()
    time.sleep(2)

    save_game()

    pygame.quit()


def collision_with_wall_snake1():
    if ((snake.elements[0][0] > WIDTH - 32 - snake.radius // 2 or snake.elements[0][0] < 32 + snake.radius // 2) or
            (snake.elements[0][1] > HEIGHT - 32 - snake.radius // 2 or snake.elements[0][1] < 32 + snake.radius // 2)):
        global looser
        looser = 'Snake #1'
        return True
    else:
        return False


def collision_with_wall_snake2():
    if ((snake2.elements[0][0] > WIDTH - 32 - snake2.radius // 2 or snake2.elements[0][0] < 32 + snake2.radius // 2) or
            (snake2.elements[0][1] > HEIGHT - 32 - snake2.radius // 2 or snake2.elements[0][1] < 32 + snake2.radius // 2)):
        global looser
        looser = 'Snake #2'
        return True
    else:
        return False


def draw_walls():
    for x in range(32, WIDTH - 32, 32):
        WIN.blit(WALL, (x, 0))
        WIN.blit(WALL, (x, HEIGHT - 32))
    for y in range(0, HEIGHT, 32):
        WIN.blit(WALL, (0, y))
        WIN.blit(WALL, (WIDTH - 32, y))


def collision_with_food_snake1():
    if (food.x in range(snake.elements[0][0] - 35, snake.elements[0][0]) and
            (food.y in range(snake.elements[0][1] - 35, snake.elements[0][1]))):
        snake.is_add = True
        food.x = random.randint(32, WIDTH - 32 - 35)
        food.y = random.randint(32, HEIGHT - 32 - 35)


def collision_with_food_snake2():
    if (food.x in range(snake2.elements[0][0] - 35, snake2.elements[0][0]) and
            (food.y in range(snake2.elements[0][1] - 35, snake2.elements[0][1]))):
        snake2.is_add = True
        food.x = random.randint(32, WIDTH - 32 - 35)
        food.y = random.randint(32, HEIGHT - 32 - 35)


def show_score(x, y, score):
    score_text = FONT.render('Score: ' + str(score), True, BLACK)
    WIN.blit(score_text, (x, y))


def draw_window():
    WIN.fill(LIGHT_GREEN)

    draw_walls()

    movement()

    snake.draw()
    snake.move()

    snake2.draw()
    snake2.move()

    collision_with_food_snake1()
    collision_with_food_snake2()

    food.draw()

    show_score(40, 35, snake.score)
    show_score(580, 35, snake2.score)


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
    elif pressed[pygame.K_d]:
        snake2.dx = VEL
        snake2.dy = 0
    elif pressed[pygame.K_a]:
        snake2.dx = -VEL
        snake2.dy = 0
    elif pressed[pygame.K_w]:
        snake2.dx = 0
        snake2.dy = -VEL
    elif pressed[pygame.K_s]:
        snake2.dx = 0
        snake2.dy = VEL


snake = Snake()
snake2 = Snake()
food = Food()
looser = 'No one'


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

        if collision_with_wall_snake1() or collision_with_wall_snake2():
            game_over()
        draw_window()
        # draw_menu()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
