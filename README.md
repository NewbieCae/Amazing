<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Press+Start+2P&size=18&pause=1000&color=BB00FF&center=true&vCenter=true&width=900&lines=INITIALIZING+A-MAZE-ING...;GENERATING+MAZE...;CALCULATING+SHORTEST+PATH...;MAZE+SYSTEM+READY..."/>
</p>

<p align="center">
  <img width="100%" src="https://capsule-render.vercel.app/api?type=rect&color=0F0F1A&height=180&section=header&text=A-Maze-ing&fontColor=C77DFF&fontSize=45&animation=fadeIn"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/language-Python-6A0DAD?style=for-the-badge" />
  <img src="https://img.shields.io/badge/algorithm-DFS%20%2B%20BFS-6A0DAD?style=for-the-badge" />
  <img src="https://img.shields.io/badge/visualization-Terminal%20%2B%20Pygame-6A0DAD?style=for-the-badge" />
  <img src="https://img.shields.io/badge/project-42-6A0DAD?style=for-the-badge" />
</p>

```txt
[ SYSTEM BOOT ]

CONFIG PARSER            [OK]
MAZE GENERATOR           [OK]
42 PATTERN               [OK]
DFS ENGINE               [OK]
BFS PATHFINDER           [OK]
HEX ENCODER              [OK]
TERMINAL DISPLAY         [OK]
PYGAME DISPLAY           [OK]
MAZEGEN PACKAGE          [OK]

> A-Maze-ing READY
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

<p align="center">

<i>Generating configurable mazes, finding the shortest path and turning algorithms into interactive visualizations.</i>

</p>

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<div align="center">

`CONFIG → DFS GENERATION → 42 PATTERN → PERFECT / PAC-MAN MODE → BFS → HEX OUTPUT → DISPLAY`

</div>

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

## DESCRIPTION

*A-Maze-ing* is a maze generation project developed as part of the **42 curriculum**.

The program generates configurable mazes, exports them using hexadecimal wall encoding, computes the shortest path between an entry and an exit, and provides a choice between interactive **Terminal** and **Pygame** visualizations.

The project includes:

- perfect maze generation;
- imperfect / Pac-Man-inspired maze generation;
- randomized iterative DFS;
- BFS shortest-path computation;
- a visible `42` pattern;
- hexadecimal wall encoding;
- reproducible generation using seeds;
- interactive Terminal visualization;
- interactive Pygame visualization;
- a reusable Python package named `mazegen`.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/OBJECTIVES-6A0DAD?style=for-the-badge" />

The purpose of this project is to understand and implement:

- maze generation algorithms;
- graph traversal;
- Depth-First Search;
- Breadth-First Search;
- pathfinding;
- seeded random generation;
- bitwise wall representation;
- configuration parsing;
- data validation;
- Python packaging;
- reusable software architecture;
- terminal rendering;
- graphical rendering;
- automated testing;
- static typing and linting.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/MAZE PIPELINE-6A0DAD?style=for-the-badge" />

<div align="center">

```txt
┌─────────────────────┐
│     config.txt      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   Config Parser     │
│ parse + validation  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│    MazeGenerator    │
│ randomized DFS      │
└──────────┬──────────┘
           │
           ├───────────────┐
           │               │
           ▼               ▼
┌────────────────┐  ┌────────────────┐
│ PERFECT=True   │  │ PERFECT=False  │
│ perfect maze   │  │ Pac-Man mode   │
└───────┬────────┘  └───────┬────────┘
        │                   │
        └─────────┬─────────┘
                  │
                  ▼
        ┌───────────────────┐
        │   BFS Pathfinder  │
        │   shortest path   │
        └─────────┬─────────┘
                  │
          ┌───────┴─────────┐
          ▼                 ▼
┌──────────────────┐  ┌──────────────────┐
│ Hexadecimal File │  │ Visual Display   │
│ maze.txt         │  │ Terminal/Pygame  │
└──────────────────┘  └──────────────────┘
```

</div>

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/KEY CONCEPT-MAZE GENERATION-6A0DAD?style=for-the-badge" />

### 📌 Randomized Depth-First Search

The main maze generation algorithm is a randomized iterative **Depth-First Search (DFS)**.

Generation starts from the configured entry cell.

```txt
ENTRY
  ↓
Find unvisited neighbors
  ↓
Choose random neighbor
  ↓
Open passage
  ↓
Push neighbor to stack
  ↓
Continue exploring
  ↓
No neighbor?
  ↓
Backtrack
  ↓
MAZE GENERATED
```

The algorithm:

1. starts at the entry;
2. finds neighboring cells that have not been visited;
3. ignores cells belonging to the `42` pattern;
4. randomly selects an available neighbor;
5. opens a passage between both cells;
6. pushes the new cell onto the stack;
7. backtracks when no neighbor is available;
8. continues until all reachable cells have been explored.

The implementation is **iterative** instead of recursive, avoiding dependence on Python's recursion depth for larger mazes.

A seeded `random.Random` instance is used so that generation can be reproduced.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

### 📌 Why DFS?

Randomized DFS naturally creates a connected spanning structure while exploring the maze.

In perfect mode, avoiding connections to already visited cells prevents cycles during the initial generation.

It is also easy to extend.

In imperfect mode, additional passages can be opened after DFS generation to introduce loops and reduce dead ends.

```txt
DFS
 │
 ├── PERFECT=True  → keep tree structure
 │
 └── PERFECT=False → open additional passages
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/PERFECT MODE-6A0DAD?style=for-the-badge" />

With:

```txt
PERFECT=True
```

the generator creates a perfect maze using randomized iterative DFS.

The resulting accessible maze contains a unique path between cells, except for the cells reserved for the closed `42` pattern.

```txt
PERFECT=True

DFS
 ↓
Connected maze
 ↓
No additional passages
 ↓
No cycles introduced
 ↓
Unique path
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/PAC--MAN MODE-6A0DAD?style=for-the-badge" />

With:

```txt
PERFECT=False
```

the maze is first generated using DFS and then modified to introduce additional passages.

The imperfect mode:

- reduces the number of dead ends;
- introduces loops;
- opens the four corners and the center when possible;
- prevents fully open `3x3` areas;
- preserves the closed cells forming the `42` pattern;
- keeps the maze connected.

```txt
DFS MAZE
   ↓
OPEN EXTRA PASSAGES
   ↓
REDUCE DEAD ENDS
   ↓
CREATE LOOPS
   ↓
CHECK 3x3 AREAS
   ↓
PAC-MAN STYLE MAZE
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/42 PATTERN-BB00FF?style=for-the-badge" />

A visible `42` is created inside the maze using fully blocked cells.

The pattern occupies a `7x5` area:

```txt
#.#.###
#.#...#
###.###
..#.#..
..#.###
```

Each `#` represents a fully closed cell.

These cells are excluded from maze generation so that no passage can cross the pattern.

```txt
NORMAL CELL → maze generation allowed

42 CELL     → █████
              CLOSED
              NO PASSAGE
```

If the maze is smaller than the minimum size required for the pattern, the pattern is omitted and a message is printed.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/SHORTEST PATH-6A0DAD?style=for-the-badge" />

The shortest path between the entry and exit is computed using **Breadth-First Search (BFS)**.

BFS explores the maze level by level.

For every discovered cell, the algorithm stores its parent.

Once the exit is reached, the path is reconstructed backwards and then reversed.

```txt
ENTRY
  ↓
BFS
  ↓
Explore neighbors level by level
  ↓
Store parent of each cell
  ↓
EXIT FOUND
  ↓
Follow parents backwards
  ↓
Reverse path
  ↓
ENTRY → ... → EXIT
```

The path is also converted into directions:

```txt
N → North
E → East
S → South
W → West
```

Example:

```txt
EESSSEENN...
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/WALL ENCODING-6A0DAD?style=for-the-badge" />

Each maze cell stores its walls as a bit mask.

| Direction | Value |
|:---:|:---:|
| North | `1` |
| East | `2` |
| South | `4` |
| West | `8` |

The existing walls are combined using bitwise OR.

Example:

```txt
North = 1
East  = 2
South = 4
West  = 8

1 + 2 + 4 + 8 = 15
```

Decimal `15` becomes:

```txt
F
```

in hexadecimal.

Therefore:

```txt
┌───┐
│   │  → N + E + S + W
└───┘  → 1 + 2 + 4 + 8
       → 15
       → F
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/CONFIGURATION-6A0DAD?style=for-the-badge" />

The program reads its parameters from a configuration file.

Example:

```txt
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```

### Configuration fields

| Key | Description |
|---|---|
| `WIDTH` | Maze width |
| `HEIGHT` | Maze height |
| `ENTRY` | Entry coordinates as `x,y` |
| `EXIT` | Exit coordinates as `x,y` |
| `OUTPUT_FILE` | Generated output file |
| `PERFECT` | Perfect or imperfect generation mode |
| `SEED` | Random generation seed |

The parser validates:

```txt
REQUIRED FIELDS        [OK]
DIMENSIONS             [OK]
COORDINATES            [OK]
INTEGER VALUES         [OK]
ENTRY != EXIT          [OK]
PERFECT BOOLEAN        [OK]
```

`PERFECT` must strictly be:

```txt
PERFECT=True
```

or:

```txt
PERFECT=False
```

Invalid values are rejected.

Example:

```txt
PERFECT=plop

> ERROR: PERFECT must be either True or False
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/INSTRUCTIONS-6A0DAD?style=for-the-badge" />

### Installation

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the project and development tools:

```bash
make install
```

### Run

```bash
make run
```

or:

```bash
python3 a_maze_ing.py config.txt
```

A different configuration file can be supplied with:

```bash
make run CONFIG=another_config.txt
```

After generation:

```txt
Choose display mode:

[1] Terminal
[2] Pygame

Choice:
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/TERMINAL MODE-6A0DAD?style=for-the-badge" />

Select:

```txt
[1] Terminal
```

The maze is displayed directly inside the terminal.

```txt
S → Start
E → Exit
. → Shortest path
```

### Controls

```txt
P → Show / hide shortest path
R → Regenerate maze
C → Change wall color
Q → Quit
```

Wall colors cycle while the program is running:

```txt
WHITE
  ↓
RED
  ↓
GREEN
  ↓
BLUE
  ↓
YELLOW
  ↓
MAGENTA
  ↓
CYAN
  ↓
WHITE
```

The terminal display can also be launched directly with:

```bash
python3 -m display.terminal
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/PYGAME MODE-6A0DAD?style=for-the-badge" />

Select:

```txt
[2] Pygame
```

The graphical interface displays:

- maze walls;
- the `42` pattern;
- start and exit positions;
- the shortest path when enabled;
- interactive controls.

### Controls

```txt
P → Show / hide shortest path
R → Regenerate maze
C → Change wall color
Q → Quit
```

The maze automatically adapts its cell size to fit inside the display area.

The Pygame interface can also be launched directly with:

```bash
python3 -m display.pygame_display
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/OUTPUT FORMAT-6A0DAD?style=for-the-badge" />

The output file contains:

```txt
1. Hexadecimal maze
2. Empty line
3. Entry coordinates
4. Exit coordinates
5. Shortest path
```

Example structure:

```txt
FFFFFFFF
...
FFFFFFFF

0,0
19,14
EESSSE...
```

The actual hexadecimal maze and path depend on the configuration and seed.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/PROJECT ARCHITECTURE-6A0DAD?style=for-the-badge" />

```txt
Amazing/
│
├── a_maze_ing.py
├── config_parser.py
├── config.txt
├── Makefile
├── pyproject.toml
├── mypy.ini
├── .flake8
├── .gitignore
├── LICENSE.md
├── README.md
├── note.md
│
├── mazegen-0.1.0-py3-none-any.whl
│
├── mazegen/
│   ├── __init__.py
│   ├── generator.py
│   └── pattern42.py
│
├── display/
│   ├── __init__.py
│   ├── terminal.py
│   └── pygame_display.py
│
└── tests/
    ├── test_pattern42.py
    └── test_pacman.py
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/KEY CODE ARCHITECTURE-6A0DAD?style=for-the-badge" />

### `a_maze_ing.py`

Main program orchestrator.

```txt
CONFIG
  ↓
PARSE
  ↓
CREATE 42 PATTERN
  ↓
CREATE MazeGenerator
  ↓
GENERATE
  ↓
WRITE OUTPUT
  ↓
SELECT DISPLAY
```

### `config_parser.py`

Responsible for:

```txt
READ CONFIG
    ↓
PARSE KEY / VALUE
    ↓
VALIDATE
    ↓
CONVERT TYPES
    ↓
RETURN CONFIGURATION
```

### `mazegen/generator.py`

Contains the main maze generation and pathfinding logic.

Responsibilities include:

- DFS generation;
- perfect / imperfect modes;
- passage creation;
- wall management;
- BFS pathfinding;
- hexadecimal grid generation.

### `mazegen/pattern42.py`

Creates and positions the closed `42` pattern.

### `display/terminal.py`

Handles the interactive ASCII terminal visualization.

### `display/pygame_display.py`

Handles the interactive graphical visualization.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/REUSABLE MAZEGEN PACKAGE-BB00FF?style=for-the-badge" />

The maze generator is provided as a reusable standalone Python package.

```txt
mazegen/
├── __init__.py
├── generator.py
└── pattern42.py
```

`MazeGenerator` is exposed directly by the package:

```python
from mazegen import MazeGenerator

maze = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit=(19, 14),
    perfect=True,
    seed=42,
)

maze.generate()
```

Main public operations:

```python
maze.generate()
maze.find_path()
maze.has_wall(x, y, direction)
maze.to_grid()
```

This allows the maze generation logic to be reused independently from the A-Maze-ing application.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/PACKAGE BUILD-6A0DAD?style=for-the-badge" />

The package configuration is defined in:

```txt
pyproject.toml
```

Build the wheel with:

```bash
make build
```

or:

```bash
python3 -m build --wheel --outdir .
```

Generated package:

```txt
mazegen-0.1.0-py3-none-any.whl
```

Install it in another environment with:

```bash
python3 -m pip install ./mazegen-0.1.0-py3-none-any.whl
```

Then:

```python
from mazegen import MazeGenerator
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/TESTING-6A0DAD?style=for-the-badge" />

The project uses `pytest`.

Run:

```bash
make test
```

or:

```bash
python3 -m pytest -v
```

The test suite verifies:

```txt
42 PATTERN CLOSED CELLS        [OK]
SMALL MAZE PATTERN HANDLING   [OK]
PAC-MAN CONNECTIVITY          [OK]
DEAD END LIMITING             [OK]
OPEN 3x3 PREVENTION           [OK]
MULTIPLE SEEDS                [OK]
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/CODE QUALITY-6A0DAD?style=for-the-badge" />

The project uses:

```txt
flake8
mypy
pytest
```

Run:

```bash
make lint
```

This executes:

```bash
flake8 .
mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
```

A stricter optional check is available:

```bash
make lint-strict
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/MAKEFILE-6A0DAD?style=for-the-badge" />

```bash
make install      # Install project and development tools
make run          # Run A-Maze-ing
make test         # Run pytest
make lint         # Run flake8 and mypy
make lint-strict  # Run stricter type checks
make build        # Build mazegen wheel
make clean        # Remove caches
make fclean       # Remove caches and build artifacts
make re           # Clean and run again
make help         # Display available Makefile commands
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

🎓 <img src="https://img.shields.io/badge/KEY WHAT THIS PROJECT TAUGHT ME-6A0DAD?style=for-the-badge" />

- implementing randomized DFS;
- understanding graph traversal;
- using BFS for shortest paths;
- understanding perfect and imperfect mazes;
- representing walls with bit masks;
- using hexadecimal encoding;
- designing reproducible algorithms with seeds;
- validating configuration files;
- building interactive terminal interfaces;
- building graphical interfaces with Pygame;
- writing reusable Python modules;
- packaging Python code;
- writing automated tests;
- using type annotations;
- using `mypy` and `flake8`;
- separating generation logic from visualization;
- designing software around reusable components.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/MENTAL SUMMARY-BB00FF?style=for-the-badge" />

```txt
I READ THE CONFIG
        ↓
I VALIDATE IT
        ↓
I BUILD THE 42 PATTERN
        ↓
I GENERATE THE MAZE WITH DFS
        ↓
I ADD LOOPS IF PERFECT=False
        ↓
I FIND THE SHORTEST PATH WITH BFS
        ↓
I ENCODE THE WALLS IN HEXADECIMAL
        ↓
I WRITE THE OUTPUT FILE
        ↓
I DISPLAY THE MAZE
        ↓
TERMINAL OR PYGAME
```

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/RESOURCES-6A0DAD?style=for-the-badge" />

Resources used during development include:

- the A-Maze-ing project subject;
- Python documentation;
- Pygame documentation;
- Wikipedia — Maze generation algorithm;
- YouTube tutorials and educational videos.

### References

- Maze generation algorithm:  
  `https://en.wikipedia.org/wiki/Maze_generation_algorithm`

- YouTube — Maze / algorithm resources:  
  `https://www.youtube.com/watch?v=i5mmGBdLOnM`

- YouTube — Maze / algorithm resources:  
  `https://www.youtube.com/watch?v=jZQ31-4_8KM`

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/AI USAGE-6A0DAD?style=for-the-badge" />

AI tools were used as development support during the project.

They were used for:

- explaining Python concepts and algorithms;
- debugging and identifying implementation issues;
- reviewing type annotations and linting errors;
- explaining Python packaging and wheel generation;
- reviewing the Pygame interface;
- reviewing project structure and documentation.

AI-generated suggestions were reviewed, adapted and tested against the actual project implementation before being kept.

The maze generation logic, project integration, testing and final validation were carried out and verified by the project authors.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<img src="https://img.shields.io/badge/LICENSE-6A0DAD?style=for-the-badge" />

This project is distributed under the **MIT License**.

See:

```txt
LICENSE.md
```

for the complete license text.

<div align="center">

⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻⸻

</div>

<div align="center">

👩🏽‍💻 **AUTHORS**

*This activity has been created as part of the 42 curriculum by **celfofan** and **mcheddad**.*

Built with Python, algorithms, mazes and patience.

`DFS → BFS → HEX → TERMINAL → PYGAME`

</div>
