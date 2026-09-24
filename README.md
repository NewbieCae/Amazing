*This activity has been created as part of the 42 curriculum by celfofan and mcheddad*
# A-Maze-ing

A-Maze-ing is a maze generation project developed as part of the 42 curriculum.

The program generates configurable mazes, exports them using hexadecimal wall encoding, computes the shortest path between an entry and an exit, and provides terminal and Pygame visualizations.

The project also includes:

- perfect and imperfect maze generation;
- a visible `42` pattern made of fully closed cells;
- a Pac-Man-inspired imperfect mode;
- shortest-path computation;
- an interactive graphical interface;
- a reusable Python package named `mazegen`.

---

## Features

### Maze generation

The maze generator supports configurable:

- width and height;
- entry and exit coordinates;
- random seed;
- perfect or imperfect generation mode;
- output file.

### Perfect mode

With:

```text
PERFECT=True
```

the generator creates the maze using a randomized iterative Depth-First Search.

The resulting maze contains a unique path between accessible cells, except for the cells reserved for the `42` pattern.

### Imperfect / Pac-Man mode

With:

```text
PERFECT=False
```

the maze is first generated using DFS and is then modified to introduce additional passages.

The imperfect mode:

- reduces the number of dead ends;
- introduces loops;
- opens the four corners and the center when possible;
- prevents fully open `3x3` areas;
- preserves the closed cells forming the `42` pattern.

---

## The `42` Pattern

A visible `42` is created inside the maze using blocked cells.

The pattern occupies a `7x5` area:

```text
#.#.###
#.#...#
###.###
..#.#..
..#.###
```

Each `#` represents a fully closed cell.

These cells are excluded from maze generation so that no passage can cross the pattern.

If the maze is smaller than the minimum size required for the pattern, the pattern is omitted and a message is printed.

---

## Maze Generation Algorithm

The main maze generation algorithm is a randomized iterative **Depth-First Search (DFS)**.

Generation starts from the configured entry cell.

The algorithm keeps a stack of visited cells:

1. Start at the entry.
2. Find neighboring cells that have not yet been visited.
3. Ignore cells belonging to the `42` pattern.
4. Randomly select one available neighbor.
5. Open a passage between the current cell and that neighbor.
6. Push the neighbor onto the stack.
7. When a cell has no available neighbor, backtrack.
8. Continue until no more cells can be explored.

An iterative implementation is used instead of recursive DFS, avoiding dependence on Python's recursion depth for larger mazes.

A seeded `random.Random` instance is used so generation can be reproducible.

---

## Why DFS?

Randomized DFS is well suited to maze generation because it naturally builds a connected spanning structure while visiting cells.

In perfect mode, avoiding connections to already visited cells prevents cycles from being introduced during the initial generation.

It is also straightforward to extend: in imperfect mode, additional passages can be opened after the initial DFS generation to create loops and reduce dead ends.

---

## Shortest Path

The shortest path between the entry and exit is computed using **Breadth-First Search (BFS)**.

BFS explores the maze level by level and stores the parent of each discovered cell.

Once the exit is reached, the path is reconstructed by following the parent relationships back to the entry.

The resulting path is then reversed to obtain:

```text
ENTRY -> ... -> EXIT
```

The path can be displayed in the interfaces and is also converted to a sequence of directions:

```text
N
E
S
W
```

---

## Wall Representation

Each maze cell stores its walls as a hexadecimal bit mask.

The wall values are:

| Direction | Value |
|-----------|------:|
| North | `1` |
| East | `2` |
| South | `4` |
| West | `8` |

The values of existing walls are combined using bitwise OR.

For example, a cell containing all four walls has:

```text
1 + 2 + 4 + 8 = 15
```

which is written in hexadecimal as:

```text
F
```

---

## Configuration

The program reads its parameters from a configuration file.

Example `config.txt`:

```text
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
|-----|-------------|
| `WIDTH` | Maze width |
| `HEIGHT` | Maze height |
| `ENTRY` | Entry coordinates as `x,y` |
| `EXIT` | Exit coordinates as `x,y` |
| `OUTPUT_FILE` | Generated output file |
| `PERFECT` | Enables or disables perfect mode |
| `SEED` | Random generation seed |

The parser checks required fields, maze dimensions, coordinates, integer values and ensures that entry and exit are different.

---

## Usage

Run the main program with:

```bash
python3 a_maze_ing.py config.txt
```

or:

```bash
make run
```

A different configuration file can be supplied with:

```bash
make run CONFIG=another_config.txt
```

The generated maze is written to the file specified by `OUTPUT_FILE`.

---

## Output Format

The output file contains:

1. the hexadecimal representation of the maze;
2. the entry coordinates;
3. the exit coordinates;
4. the shortest path encoded using `N`, `E`, `S`, and `W`.

Example structure:

```text
FFFFFFFF
...
FFFFFFFF

0,0
19,14
EESSSE...
```

The actual hexadecimal maze and path depend on the configuration and seed.

---

## Terminal Display

A terminal interface is available in:

```text
display/terminal.py
```

Run it with:

```bash
python3 -m display.terminal
```

Controls:

```text
P - Show / hide the shortest path
R - Regenerate the maze
Q - Quit
```

The terminal uses:

```text
S - Start
E - Exit
. - Shortest path
```

---

## Pygame Display

An interactive graphical visualization is available using Pygame.

Run:

```bash
python3 -m display.pygame_display
```

The graphical interface displays:

- maze walls;
- the `42` pattern;
- start and exit positions;
- the shortest path when enabled;
- interactive controls.

Controls:

```text
P - Show / hide shortest path
R - Regenerate maze
C - Change wall color
Q - Quit
```

The maze automatically adapts its cell size to fit inside the display area.

---

## Reusable `mazegen` Package

The maze generator is also provided as a standalone reusable Python package.

Package structure:

```text
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

The main public operations include:

```python
maze.generate()
maze.find_path()
maze.has_wall(x, y, direction)
maze.to_grid()
```

---

## Building the Package

The package configuration is defined in:

```text
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

The resulting package follows the required naming convention:

```text
mazegen-0.1.0-py3-none-any.whl
```

It can be installed in another environment with:

```bash
python3 -m pip install ./mazegen-0.1.0-py3-none-any.whl
```

and imported with:

```python
from mazegen import MazeGenerator
```

---

## Tests

The project uses `pytest`.

Run all tests with:

```bash
make test
```

or:

```bash
python3 -m pytest -v
```

The current test suite verifies:

- the `42` pattern contains the expected blocked cells;
- every `42` cell remains fully closed;
- the pattern is omitted when the maze is too small;
- imperfect mode remains connected;
- imperfect mode limits dead ends;
- no fully open `3x3` area is created.

The tests are executed across multiple seeds to check generation behavior under different random configurations.

---

## Code Quality

The project uses both `flake8` and `mypy`.

Run:

```bash
make lint
```

This performs:

```bash
flake8 .
mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
```

A stricter optional check is also available:

```bash
make lint-strict
```

---

## Project Structure

```text
Amazing/
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

---

## Makefile

Useful commands:

```bash
make run          # Run the maze generator
make test         # Run pytest
make lint         # Run flake8 and mypy
make lint-strict  # Run stricter type checks
make build        # Build the mazegen wheel
make clean        # Remove caches
make fclean       # Remove caches and build artifacts
make re           # Clean and run again
make help         # Display available Makefile commands
```

---

## Resources

Resources used during development include:

- the A-Maze-ing project subject;
- Python documentation for the standard library features used by the project;
- Pygame documentation for the graphical interface.
- Wikipedia:
  - https://en.wikipedia.org/wiki/Maze_generation_algorithm
  -
- YouTube tutorials and educational videos:
  - https://www.youtube.com/watch?v=i5mmGBdLOnM
  - https://www.youtube.com/watch?v=jZQ31-4_8KM
  - https://www.youtube.com/watch?v=uctN47p_KVk

These resources were used to better understand maze generation,
algorithms, Python concepts, and the implementation of the project.
---

## AI Usage

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

---

## License

This project is distributed under the MIT License.

See:

```text
LICENSE.md
```

for the complete license text.