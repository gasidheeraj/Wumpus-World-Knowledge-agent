# src/agent.py

def decide_next_move(world):
    x, y = world.agent_pos
    print(f"Agent is at ({x}, {y})")

    if (x, y) == world.gold_pos:
        print("Gold found! Agent wins!")
        return "WIN"

    world.safe_cells.add((x, y))
    world.visited.add((x, y))

    for nx, ny in world.get_neighbors(x, y):
        if (nx, ny) not in world.visited:
            if (nx, ny) not in world.safe_cells:
                world.update_kb(nx, ny)

    world.infer_safe_cells()

    for cell in world.safe_cells:
        if cell not in world.visited:
            world.agent_pos = cell
            return "MOVE"

    uncertain = world.assess_risks()
    if uncertain:
        world.agent_pos = uncertain[0]
        return "RISK_MOVE"

    return "STUCK"
