import pygame
import random

pygame.init()

WINDOW_SIZE = WIDTH, HEIGHT = 600, 600
WINDOW = pygame.display.set_mode(WINDOW_SIZE)


class Snake:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH / 2) - 20, (HEIGHT / 2) - 20, 20, 20)

        self.xSpeed = 1
        self.ySpeed = 0

        self.size = 0
        self.body = []

    def draw(self):
        for part in self.body:
            pygame.draw.rect(WINDOW, (255, 255, 255), part)
        pygame.draw.rect(WINDOW, (255, 255, 255), self.rect)

    def move(self, x, y):
        self.xSpeed = x
        self.ySpeed = y

    def eat(self, f):
        if self.rect.colliderect(f.rect):
            self.body.append(pygame.Rect(self.rect.x, self.rect.y, 20, 20))
            self.size += 1
            return True
        else:
            return False

    def update(self):
        if self.size > 0:
            for i in range(0, self.size - 1):
                self.body[i] = self.body[i + 1]
            self.body[self.size - 1] = pygame.Rect(self.rect.x, self.rect.y, 20, 20)
        if WIDTH > self.rect.x + self.xSpeed * 20 > -20 and HEIGHT > self.rect.y + self.ySpeed * 20 > -20:
            self.rect.x += self.xSpeed * 20
            self.rect.y += self.ySpeed * 20


class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x, self.y, 20, 20)

        self.new_pos()

    def new_pos(self):
        self.x = random.randrange(0, WIDTH / 20)
        self.y = random.randrange(0, HEIGHT / 20)
        self.rect.x = self.x * 20
        self.rect.y = self.y * 20

    def draw(self):
        pygame.draw.rect(WINDOW, (255, 0, 100), self.rect)


player = Snake()
food = Food()
Clock = pygame.time.Clock()
loop_counter = 0

game_loop = True
while game_loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) == 'up':
                player.move(0, -1)
            if pygame.key.name(event.key) == 'down':
                player.move(0, 1)
            if pygame.key.name(event.key) == 'left':
                player.move(-1, 0)
            if pygame.key.name(event.key) == 'right':
                player.move(1, 0)

    if loop_counter % 10 == 0:
        player.update()

    if player.eat(food):
        food.new_pos()

    WINDOW.fill((0, 0, 0))

    player.draw()
    food.draw()
    pygame.display.update()

    loop_counter += 1
    Clock.tick(60)

pygame.quit()
