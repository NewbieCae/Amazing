from mazegen import MazeGenerator
from mazegen.pattern42 import create_pattern42

def display_maze(maze, show_path: bool = False) -> None:
    """Affiche le labyrinthe dans le terminal."""
    for y in range(maze.height):

        for x in range(maze.width):
            if maze.has_wall(x, y, "N"):
                print("+---", end="")
            else:
                print("+   ", end="")
        print("+")

        print("|", end="")
        for x in range(maze.width):
            print(cell_entry_exit(maze, x, y, show_path), end="")

            if maze.has_wall(x, y, "E"):
                print("|", end="")
            else:
                print(" ", end="")
        print()

    for x in range(maze.width):
        if maze.has_wall(x, maze.height - 1, "S"):
            print("+---", end="")
        else:
            print("+   ", end="")
    print("+")


def cell_entry_exit(maze, x: int, y:int, show_path: bool = False) -> str:
    path = maze.find_path()

    if (x, y) == maze.entry:
        return " E "
    elif (x,y) == maze.exit:
        return " S "
    elif show_path and path and (x, y) in path:
        return " . "
    else:
        return "   "


def terminal_menu(maze) -> None:
    show_path = False

    while True:
        display_maze(maze, show_path)
        print()
        print("[P] Afficher / masquer le chemin")
        print("[R] Regenerer le labyrinthe")
        print("[Q] Quitter")

        choice = input("choix: ").strip().lower()

        if choice == "p":
            show_path = not show_path
        elif choice == "r":
            maze.generate()
        elif choice == "q":
            break
        else:
            print("Choix invalide")

if __name__ == "__main__":
    blocked = create_pattern42(20, 15)

    maze = MazeGenerator(
        width=20,
        height=15,
        entry=(0,0),
        exit=(19,14),
        perfect=False,
        seed=10,
        blocked=blocked
    )

    maze.generate()
    dead_ends = 0
    for y in range(maze.height):
        for x in range(maze.width):
            if maze._open_count(x,y) == 1:
                dead_ends += 1
    print("dead ends:", dead_ends)
    print("open 3x3:", maze._has_open_3x3())
    terminal_menu(maze)
    