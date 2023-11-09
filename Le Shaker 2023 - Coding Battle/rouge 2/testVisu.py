import pygame
import sys

pygame.init()

WINDOW_WIDTH = WINDOW_HEIGHT = 800
CELL_SIZE = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def draw_grid(screen, data, xCurrent, yCurrent):
    screen.fill(WHITE)
    for x, y, h in data:
        pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        font = pygame.font.Font(None, 36)
        text = font.render(str(h), True, WHITE)
        text_rect = text.get_rect(center=(x * CELL_SIZE + CELL_SIZE / 2, y * CELL_SIZE + CELL_SIZE / 2))
        screen.blit(text, text_rect)
        if x == xCurrent and y == yCurrent:
            deltaplane = pygame.draw.circle(screen, RED,
                                            (x * CELL_SIZE + CELL_SIZE / 2, y * CELL_SIZE + CELL_SIZE / 2), 3)


def show(rawDataForest, xCurrent, yCurrent):
    data = []
    for y, line in enumerate(rawDataForest):
        for x, h in enumerate(line):
            data.append((x, y, h))
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Quadrillage Pygame")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_grid(screen, data, xCurrent, yCurrent)
        pygame.display.flip()
