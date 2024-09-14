import pygame
import random
from collections import deque

# Ініціалізація Pygame
pygame.init()

# Налаштування екрану
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pacman Game")

# Налаштування кольорів
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Розмір комірок
cell_size = 20
rows = screen_height // cell_size
cols = screen_width // cell_size

# Клас для лабіринту
class Maze:
    def __init__(self):
        self.grid = [[1 for _ in range(cols)] for _ in range(rows)]
        self.food = []
        self.generate_maze()
        self.place_food()

    # Алгоритм пошуку в глибину для генерації деревоподібного лабіринту
    def generate_maze(self):
        start = (1, 1)
        stack = [start]
        self.grid[start[0]][start[1]] = 0

        while stack:
            current = stack[-1]
            neighbors = []

            # Перевірка сусідів по вертикалі та горизонталі через одну клітинку
            for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]:
                nx, ny = current[0] + dx, current[1] + dy
                if 1 <= nx < rows-1 and 1 <= ny < cols-1 and self.grid[nx][ny] == 1:
                    neighbors.append((nx, ny))

            if neighbors:
                chosen = random.choice(neighbors)
                mid_x, mid_y = (current[0] + chosen[0]) // 2, (current[1] + chosen[1]) // 2
                self.grid[chosen[0]][chosen[1]] = 0
                self.grid[mid_x][mid_y] = 0
                stack.append(chosen)
            else:
                stack.pop()

    def place_food(self):
        self.food.clear()
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j] == 0:
                    self.food.append((i, j))

    def draw(self, screen):
        for i in range(rows):
            for j in range(cols):
                if self.grid[i][j] == 1:
                    pygame.draw.rect(screen, BLUE, (j * cell_size, i * cell_size, cell_size, cell_size))

        # Малюємо їжу
        for f in self.food:
            pygame.draw.circle(screen, GREEN, (f[1] * cell_size + cell_size // 2, f[0] * cell_size + cell_size // 2), cell_size // 4)

# Клас для Пакмена
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def move(self, maze):
        if 0 <= self.x + self.dx < cols and 0 <= self.y + self.dy < rows:
            if maze.grid[self.y + self.dy][self.x + self.dx] == 0:
                self.x += self.dx
                self.y += self.dy

    def eat_food(self, maze):
        if (self.y, self.x) in maze.food:
            maze.food.remove((self.y, self.x))

    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (self.x * cell_size + cell_size // 2, self.y * cell_size + cell_size // 2), cell_size // 2)

# BFS Алгоритм для пошуку шляху привидів
def bfs(maze, start, goal):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols and maze.grid[neighbor[1]][neighbor[0]] == 0:
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

    return []

# Клас для Привидів
class Ghost:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.path = []

    def move(self, maze, pacman):
        if not self.path:
            self.path = bfs(maze, (self.x, self.y), (pacman.x, pacman.y))
        if self.path:
            next_pos = self.path.pop(0)
            self.x, self.y = next_pos

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x * cell_size + cell_size // 2, self.y * cell_size + cell_size // 2), cell_size // 2)

# Перевірка на зіткнення між Пакменом і привидом
def check_collision(pacman, ghost):
    return pacman.x == ghost.x and pacman.y == ghost.y

# Ініціалізація гри
level = 1
maze = Maze()
pacman = Pacman(1, 1)
ghosts = [Ghost(random.randint(0, cols-1), random.randint(0, rows-1), RED)]
font = pygame.font.SysFont(None, 36)
game_over = False

# Функція для відображення тексту на екрані
def draw_text(text, x, y, screen):
    img = font.render(text, True, WHITE)
    screen.blit(img, (x, y))

# Головний цикл гри
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Перевірка на перезапуск гри
        if game_over:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # Перезапуск гри після програшу
                level = 1
                maze = Maze()
                pacman = Pacman(1, 1)
                ghosts = [Ghost(random.randint(0, cols-1), random.randint(0, rows-1), RED)]
                game_over = False
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.dx, pacman.dy = -1, 0
                elif event.key == pygame.K_RIGHT:
                    pacman.dx, pacman.dy = 1, 0
                elif event.key == pygame.K_UP:
                    pacman.dx, pacman.dy = 0, -1
                elif event.key == pygame.K_DOWN:
                    pacman.dx, pacman.dy = 0, 1

    if not game_over:
        # Оновлення положення Пакмена і привидів
        pacman.move(maze)
        pacman.eat_food(maze)
        for ghost in ghosts:
            ghost.move(maze, pacman)

        # Перевірка на програш (зіткнення з привидом)
        for ghost in ghosts:
            if check_collision(pacman, ghost):
                game_over = True

        # Якщо вся їжа з'їдена — новий рівень
        if len(maze.food) == 0:
            level += 1
            maze = Maze()
            pacman = Pacman(1, 1)
            ghosts = [Ghost(random.randint(0, cols-1), random.randint(0, rows-1), RED)]

    # Малювання
    screen.fill(BLACK)
    maze.draw(screen)
    pacman.draw(screen)
    for ghost in ghosts:
        ghost.draw(screen)

    # Інтерфейс: рівень та кількість залишкової їжі
    draw_text(f"Level: {level}", 10, 10, screen)
    draw_text(f"Food left: {len(maze.food)}", 10, 50, screen)

    if game_over:
        draw_text("Game Over! Press R to restart", screen_width // 4, screen_height // 2, screen)

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
