from mock_maze import MockMaze

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
    maze = MockMaze()
    terminal_menu(maze)