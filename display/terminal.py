from mock_maze import MockMaze

def display_maze(maze) -> None:
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
            print(cell_entry_exit(maze, x, y), end="")

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


def cell_entry_exit(maze, x: int, y:int) -> str:
    if (x, y) == maze.entry:
        return " E "
    elif (x,y) == maze.exit:
        return " S "
    else:
        return "   "


if __name__ == "__main__":
    maze = MockMaze()
    display_maze(maze)