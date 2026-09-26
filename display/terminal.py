from mazegen import MazeGenerator
from mazegen.pattern42 import create_pattern42

WALL_COLORS = [
    "\033[97m",  # White
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[94m",  # Blue
    "\033[93m",  # Yellow
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]

RESET_COLOR = "\033[0m"


def display_maze(
    maze: MazeGenerator,
    show_path: bool = False,
    wall_color: str = "\033[97m",
) -> None:

    """Affiche le labyrinthe dans le terminal."""
    for y in range(maze.height):
        for x in range(maze.width):
            if maze.has_wall(x, y, "N"):
                print(f"{wall_color}+---{RESET_COLOR}", end="")
            else:
                print(f"{wall_color}+{RESET_COLOR}   ", end="")
        print(f"{wall_color}+{RESET_COLOR}")
        print(f"{wall_color}|{RESET_COLOR}", end="")
        for x in range(maze.width):
            print(cell_entry_exit(maze, x, y, show_path), end="")
            if maze.has_wall(x, y, "E"):
                print(f"{wall_color}|{RESET_COLOR}", end="")
            else:
                print(" ", end="")
        print()

    for x in range(maze.width):
        if maze.has_wall(x, maze.height - 1, "S"):
            print(f"{wall_color}+---{RESET_COLOR}", end="")
        else:
            print(f"{wall_color}+{RESET_COLOR}   ", end="")

    print(f"{wall_color}+{RESET_COLOR}")


def cell_entry_exit(maze: MazeGenerator, x: int, y: int,
                    show_path: bool = False) -> str:

    path = maze.find_path()

    if (x, y) == maze.entry:
        return " S "
    elif (x, y) == maze.exit:
        return " E "
    elif show_path and path and (x, y) in path:
        return " . "
    else:
        return "   "


def terminal_menu(maze: MazeGenerator) -> None:
    show_path = False
    wall_color_index = 0

    while True:
        display_maze(
            maze,
            show_path,
            WALL_COLORS[wall_color_index],
        )

        print()
        print("[P] Afficher / masquer le chemin")
        print("[R] Regenerer le labyrinthe")
        print("[C] Changer la couleur des murs")
        print("[Q] Quitter")

        choice = input("choix: ").strip().lower()

        if choice == "p":
            show_path = not show_path
        elif choice == "r":
            maze.generate()
        elif choice == "c":
            wall_color_index = (
                wall_color_index + 1
            ) % len(WALL_COLORS)
        elif choice == "q":
            break
        else:
            print("Choix invalide")


if __name__ == "__main__":
    blocked = create_pattern42(20, 15)

    maze = MazeGenerator(
        width=20,
        height=15,
        entry=(0, 0),
        exit=(19, 14),
        perfect=False,
        seed=10,
        blocked=blocked
    )

    maze.generate()
    dead_ends = 0
    for y in range(maze.height):
        for x in range(maze.width):
            if maze._open_count(x, y) == 1:
                dead_ends += 1

    print("dead ends:", dead_ends)
    print("open 3x3:", maze._has_open_3x3())

    terminal_menu(maze)
