GRID_SIZE = 4

def neighbors(x, y):
    return [
        (x + dx, y + dy)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
        if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE
    ]
