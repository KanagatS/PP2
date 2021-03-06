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

WALL = pygame.image.load('Pictures/wall.png')

FRUITS = []
for i in range(3):
    FRUITS.append(pygame.image.load(f'Pictures/fruit_{i}.png'))

FONT = pygame.font.SysFont('Courier', 35)
FONT_2 = pygame.font.SysFont('Arial', 48)

FPS = 60
VEL = 8


class Food():
    def __init__(self):
        self.x = random.randint(32, WIDTH - 32 - 35)
        self.y = random.randint(32, HEIGHT - 32 - 35)
        self.image = random.choice(FRUITS)
        self.image = pygame.transform.scale(self.image, (35, 35))

    def draw(self):
        WIN.blit(self.image, (self.x, self.y))


class Snake():
    def __init__(self):
        self.size = 3
        self.radius = 10
        self.dx = VEL
        self.dy = 0
        self.elements = [[100, 100], [120, 100], [140, 100]]
        self.score = 0
        self.is_add = False
        self.dir = 'right'

    def draw(self):
        for element in self.elements[1:]:
            pygame.draw.circle(WIN, BLACK, element, self.radius)

    def move(self):
        if self.is_add:
            self.addSnake()

        for i in range(self.size - 1, 0, -1):
            self.elements[i][0] = self.elements[i - 1][0]
            self.elements[i][1] = self.elements[i - 1][1]

        self.elements[0][0] += self.dx
        self.elements[0][1] += self.dy

        if self.elements[0][0] > WIDTH:
            self.elements[0][0] = 0
        elif self.elements[0][0] < 0:
            self.elements[0][0] = WIDTH
        elif self.elements[0][1] > HEIGHT:
            self.elements[0][1] = 0
        elif self.elements[0][1] < 0:
            self.elements[0][1] = HEIGHT

    def addSnake(self):
        self.size += 1
        self.score += 1
        self.elements.append([0, 0])
        self.is_add = False


def save_game():
    cur_time = time.strftime('%H:%M:%S', time.localtime())
    
    f = open('SavedGames.txt', 'a')
    
    f.write(f'Multi player game on hard map was played at {cur_time} with a scores of {snake.score} and {snake2.score}.\n\n')
    
    f.close()


def game_over():
    WIN.fill(RED)

    GAMEOVER_TEXT = FONT_2.render('GAME OVER!', True, BLACK)
    SCORE_TEXT1 = FONT_2.render(
        'Score of snake #1: ' + str(snake.score), True, BLACK)
    SCORE_TEXT2 = FONT_2.render(
        'Score of snake #2: ' + str(snake2.score), True, BLACK)
    LOOSER_TEXT = FONT_2.render('Loser is - ' + str(looser), True, BLACK)

    WIN.blit(GAMEOVER_TEXT, (200, 200))
    WIN.blit(SCORE_TEXT1, (200, 300))
    WIN.blit(SCORE_TEXT2, (200, 400))
    WIN.blit(LOOSER_TEXT, (200, 500))

    pygame.display.update()
    time.sleep(5)

    save_game()

    pygame.quit()


def collision_with_tail_snake1():
    if (snake.elements[0] in snake.elements[1:]):
        global looser
        looser = 'Snake #1'
        return True
    else:
        return False


def collision_with_tail_snake2():
    if (snake2.elements[0] in snake2.elements[1:]):
        global looser
        looser = 'Snake #2'
        return True
    else:
        return False


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
    for x in range(100 + 32 + 32, WIDTH - 32 - 100 - 32, 32):
        WIN.blit(WALL, (x, 150))
        WIN.blit(WALL, (x, 379))
        WIN.blit(WALL, (x, HEIGHT - 32 - 118 - 32))
    for y in range(0, HEIGHT, 32):
        WIN.blit(WALL, (0, y))
        WIN.blit(WALL, (WIDTH - 32, y))


def collision_with_food(obj):
    if (food.x in range(obj.elements[0][0] - 35, obj.elements[0][0]) and (food.y in range(obj.elements[0][1] - 35, obj.elements[0][1]))):
        obj.is_add = True
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

    collision_with_food(snake)
    collision_with_food(snake2)

    food.draw()

    show_score(40, 35, snake.score)
    show_score(580, 35, snake2.score)


def movement():
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_RIGHT] and snake.dir != 'left':
        snake.dx = VEL
        snake.dy = 0
        snake.dir = 'right'
    elif pressed[pygame.K_LEFT] and snake.dir != 'right':
        snake.dx = -VEL
        snake.dy = 0
        snake.dir = 'left'
    elif pressed[pygame.K_UP] and snake.dir != 'down':
        snake.dx = 0
        snake.dy = -VEL
        snake.dir = 'up'
    elif pressed[pygame.K_DOWN] and snake.dir != 'up':
        snake.dx = 0
        snake.dy = VEL
        snake.dir = 'down'

    elif pressed[pygame.K_d] and snake2.dir != 'left':
        snake2.dx = VEL
        snake2.dy = 0
        snake2.dir = 'right'
    elif pressed[pygame.K_a] and snake2.dir != 'right':
        snake2.dx = -VEL
        snake2.dy = 0
        snake2.dir = 'left'
    elif pressed[pygame.K_w] and snake2.dir != 'down':
        snake2.dx = 0
        snake2.dy = -VEL
        snake2.dir = 'up'
    elif pressed[pygame.K_s] and snake2.dir != 'up':
        snake2.dx = 0
        snake2.dy = VEL
        snake2.dir = 'down'


snake, snake2 = Snake(), Snake()
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
                    save_game()

        if collision_with_wall_snake1() or collision_with_tail_snake1() or collision_with_wall_snake2() or collision_with_tail_snake2():
            game_over()

        draw_window()
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == '__main__':
    main()
