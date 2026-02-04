# src/environment.py

from src.knowledge_base import KnowledgeBase
from src.utils import neighbors


class WumpusWorld:
    """
    Represents the Wumpus World environment.
    Handles world configuration, percept generation,
    knowledge base updates, and environment state.
    """

    def __init__(self, grid_size=4):
        self.GRID_SIZE = grid_size

        # World state
        self.agent_pos = (3, 0)   # Starting position
        self.gold_pos = None
        self.wumpus_pos = None
        self.pits = []

        # Percepts
        self.breezes = []
        self.stenches = []

        # Agent knowledge
        self.visited = set()
        self.safe_cells = set([(3, 0)])
        self.kb = KnowledgeBase()

    # ------------------------------------------------------------------
    # WORLD CONFIGURATION
    # ------------------------------------------------------------------

    def configure_world(self):
        """
        Hard-coded configuration for reproducibility.
        Can be randomized later if needed.
        """
        self.wumpus_pos = (1, 2)
        self.gold_pos = (2, 3)
        self.pits = [(0, 3), (2, 0), (3, 2)]

        self.generate_percepts()

    def generate_percepts(self):
        """
        Generate breeze and stench percepts based on pits and wumpus.
        """
        self.breezes = []
        self.stenches = []

        # Breeze near pits
        for pit in self.pits:
            for neighbor in neighbors(*pit):
                if neighbor not in self.pits:
                    self.breezes.append(neighbor)

        # Stench near Wumpus
        for neighbor in neighbors(*self.wumpus_pos):
            if neighbor != self.wumpus_pos:
                self.stenches.append(neighbor)

    # ------------------------------------------------------------------
    # KNOWLEDGE BASE UPDATES
    # ------------------------------------------------------------------

    def update_kb(self, x, y):
        """
        Update knowledge base based on percepts at (x, y).
        """
        percepts = []

        if (x, y) in self.breezes:
            percepts.append("breeze")
        if (x, y) in self.stenches:
            percepts.append("stench")
        if (x, y) == self.gold_pos:
            percepts.append("glitter")

        print(f"Percepts at ({x}, {y}): {', '.join(percepts) if percepts else 'None'}")

        if "breeze" in percepts:
            self.kb.add_clause(f"Pit near ({x}, {y})")

        if "stench" in percepts:
            self.kb.add_clause(f"Wumpus near ({x}, {y})")

        print("Knowledge Base:")
        for clause in self.kb.clauses:
            print(f"  - {clause}")

    # ------------------------------------------------------------------
    # INFERENCE & RISK ASSESSMENT
    # ------------------------------------------------------------------

    def infer_safe_cells(self):
        """
        Infer safe cells when no breeze or stench is perceived.
        """
        for x, y in self.visited:
            if (x, y) not in self.breezes and (x, y) not in self.stenches:
                for nx, ny in neighbors(x, y):
                    if (nx, ny) not in self.visited:
                        if (nx, ny) not in self.safe_cells:
                            print(f"Inferred safe cell: ({nx}, {ny})")
                            self.safe_cells.add((nx, ny))

    def assess_risks(self):
        """
        Assign risk scores to uncertain cells.
        Returns a list of cells sorted by lowest risk.
        """
        risks = {}

        for x, y in self.visited:
            if (x, y) in self.breezes or (x, y) in self.stenches:
                for nx, ny in neighbors(x, y):
                    if (nx, ny) not in self.visited and (nx, ny) not in self.safe_cells:
                        risks[(nx, ny)] = risks.get((nx, ny), 0) + 1

        return sorted(risks.keys(), key=lambda cell: risks[cell])

    # ------------------------------------------------------------------
    # AGENT MOVEMENT (KEEP THIS IF YOU SKIP STEP 4)
    # ------------------------------------------------------------------

    def move_agent(self):
        """
        Controls agent movement and decision-making.
        This method can be removed if agent logic is separated.
        """
        x, y = self.agent_pos
        print(f"Agent is at ({x}, {y})")

        # Win condition
        if (x, y) == self.gold_pos:
            print("Gold found! Agent wins!")
            return "WIN"

        # Update knowledge
        self.safe_cells.add((x, y))
        self.visited.add((x, y))

        for nx, ny in neighbors(x, y):
            if (nx, ny) not in self.visited:
                if (nx, ny) not in self.safe_cells:
                    self.update_kb(nx, ny)

        self.infer_safe_cells()

        # Move to known safe cell
        for cell in self.safe_cells:
            if cell not in self.visited:
                self.agent_pos = cell
                return "MOVE"

        # Explore least risky uncertain cell
        uncertain = self.assess_risks()
        if uncertain:
            next_cell = uncertain[0]
            print(f"Exploring uncertain cell: {next_cell}")
            self.agent_pos = next_cell
            return "RISK_MOVE"

        print("No moves left. Agent is stuck.")
        return "STUCK"

    # ------------------------------------------------------------------
    # OPTIONAL HELPERS (FOR STEP 4 AGENT SEPARATION)
    # ------------------------------------------------------------------

    def get_neighbors(self, x, y):
        """Helper for agent module."""
        return neighbors(x, y)
