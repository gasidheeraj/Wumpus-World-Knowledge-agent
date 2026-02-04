# main.py

import pygame
import sys

from src.environment import WumpusWorld
from src.agent import decide_next_move
from src.renderer import draw_grid, load_images


# -----------------------------
# CONFIGURATION
# -----------------------------
CELL_SIZE = 100
GRID_SIZE = 4
SCREEN_SIZE = CELL_SIZE * GRID_SIZE
FPS = 1


# -----------------------------
# PYGAME INITIALIZATION
# -----------------------------
pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Wumpus World - Knowledge-Based Agent")
clock = pygame.time.Clock()

images = load_images(CELL_SIZE)


# -----------------------------
# MAIN LOOP
# -----------------------------
def main():
    world = WumpusWorld()
    world.configure_world()

    running = True
    while running:
        screen.fill((255, 255, 255))

        # Render world
        draw_grid(world, screen, images, CELL_SIZE, GRID_SIZE)

        # Handle quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Agent decision step
        status = decide_next_move(world)

        if status == "WIN":
            print("Simulation finished: Agent found the gold.")
            running = False

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


# -----------------------------
# ENTRY POINT
# -----------------------------
if __name__ == "__main__":
    main()
