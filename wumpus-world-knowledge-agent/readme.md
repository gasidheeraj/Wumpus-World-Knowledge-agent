# Wumpus World Simulation using a Knowledge-Based Agent


## Overview
This project implements the classical Wumpus World problem using a knowledge-based artificial
intelligence agent. The agent operates in a partially observable grid environment, perceives local sensory inputs (breeze, stench, glitter), performs logical inference, and autonomously navigates the environment to safely find the gold while avoiding hazards.




## Objectives
- Design an autonomous intelligent agent capable of reasoning under uncertainty
- Apply knowledge-based reasoning instead of machine learning
- Demonstrate logical inference using percepts
- Safely explore the environment and reach the goal (gold)



Environment Description
- Grid size: 4 × 4
- Pits generate breeze in adjacent cells
- Wumpus generates stench in adjacent cells
- Gold produces glitter in the cell
- Agent starts at position (3, 0) with no prior knowledge



## Agent Behavior
The agent perceives local sensory inputs, updates a knowledge base with logical constraints, infers safe cells, and explores uncertain regions using risk-based reasoning until the gold is found.


## Project Architecture
The project follows an agent–environment architecture with clear separation of concerns: agent
logic, environment dynamics, knowledge representation, visualization, and orchestration.


WumpusWorldProject/
│
├── README.md                         # Main project documentation (GitHub)
├── requirements.txt                  # Project dependencies
├── main.py                           # Entry point to run the simulation
│
├── assets/                           # Static assets (images)
│   ├── agent.png
│   ├── wumpus.png
│   ├── gold.png
│   ├── pit.png
│   ├── breeze.png
│   └── stench.png
│
└── src/                              # Source code (Python package)
    ├── __init__.py                  # Marks src as a Python package (empty)
    ├── agent.py                     # Agent decision-making logic
    ├── environment.py               # Wumpus World environment & percepts
    ├── knowledge_base.py            # Knowledge Base & logical reasoning
    ├── renderer.py                  # Pygame visualization
    └── utils.py                     # Helper functions (neighbors, etc.)

## Installation and Setup
Follow the steps below to set up and run the project:

### Prerequisites
- Python 3.9 or higher
- `pip` package manager


## Key Files
- **`main.py`**: Contains the core logic for the Wumpus World simulation, including the PL-Resolution implementation and agent decision-making.
- **`requirements.txt`**: Lists all Python dependencies required to run the project.
- **Assets**: Contains graphical resources for the simulation, such as images for the agent, Wumpus, pits, gold, and percepts.



# References
1. Russell, S., & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th Edition). Pearson.
2. Genesereth, M. R., & Nilsson, N. J. (1987). *Logical Foundations of Artificial Intelligence*. Morgan Kaufmann.
3. Kautz, H., & Selman, B. (1992). Planning as Satisfiability. *Proceedings of the 10th European Conference on Artificial Intelligence*.




## Future Improvements
- Extend the simulation to larger grid sizes.
- Incorporate probabilistic reasoning for uncertainty.
- Allow users to configure hazards dynamically.


