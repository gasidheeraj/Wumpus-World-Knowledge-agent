# src/renderer.py

import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)


def load_images(cell_size):
    images = {
        "agent": pygame.transform.scale(
            pygame.image.load("assets/agent.png"), (cell_size, cell_size)
        ),
        "wumpus": pygame.transform.scale(
            pygame.image.load("assets/wumpus.png"), (cell_size, cell_size)
        ),
        "gold": pygame.transform.scale(
            pygame.image.load("assets/gold.png"), (cell_size, cell_size)
        ),
        "pit": pygame.transform.scale(
            pygame.image.load("assets/pit.png"), (cell_size, cell_size)
        ),
        "breeze": pygame.transform.scale(
            pygame.image.load("assets/breeze.png"), (cell_size // 2, cell_size // 2)
        ),
        "stench": pygame.transform.scale(
            pygame.image.load("assets/stench.png"), (cell_size // 2, cell_size // 2)
        ),
    }
    return images


def draw_grid(world, screen, images, cell_size, grid_size):
    for x in range(grid_size):
        for y in range(grid_size):
            rect = pygame.Rect(
                y * cell_size, x * cell_size, cell_size, cell_size
            )
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 2)

            if (x, y) == world.agent_pos:
                screen.blit(images["agent"], rect)
            elif (x, y) == world.gold_pos:
                screen.blit(images["gold"], rect)
            elif (x, y) == world.wumpus_pos:
                screen.blit(images["wumpus"], rect)
            elif (x, y) in world.pits:
                screen.blit(images["pit"], rect)

            if (x, y) in world.breezes:
                screen.blit(images["breeze"], (y * cell_size + 25, x * cell_size + 25))
            if (x, y) in world.stenches:
                screen.blit(images["stench"], (y * cell_size + 25, x * cell_size + 50))
