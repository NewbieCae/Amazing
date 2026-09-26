import sys
from config_parser import parse_config, convert_config, ConfigError
from mazegen import MazeGenerator
from mazegen.pattern42 import create_pattern42
from display.pygame_display import run_pygame
from display.terminal import terminal_menu


DELTA_TO_LETTER = {
    (0, -1): "N",
    (1, 0): "E",
    (0, 1): "S",
    (-1, 0): "W",
}


def path_to_letters(path: list[tuple[int, int]]) -> str:
    """Convertit un chemin de cellules en suite de lettres N/E/S/W."""
    lettres: list[str] = []
    for i in range(len(path) - 1):
        a = path[i]
        b = path[i + 1]
        dx = b[0] - a[0]
        dy = b[1] - a[1]
        lettres.append(DELTA_TO_LETTER[(dx, dy)])
    return "".join(lettres)


def write_output(maze: MazeGenerator, filename: str) -> None:
    """Ecrit le labyrinthe dans le fichier de sortie."""
    with open(filename, "w") as f:
        for ligne in maze.to_grid():
            chars: list[str] = []
            for valeur in ligne:
                chars.append(f"{valeur:X}")
            f.write("".join(chars) + "\n")
        f.write("\n")
        f.write(f"{maze.entry[0]},{maze.entry[1]}\n")
        f.write(f"{maze.exit[0]},{maze.exit[1]}\n")
        chemin = maze.find_path()
        if chemin is not None:
            f.write(path_to_letters(chemin) + "\n")
        else:
            f.write("\n")


def choose_display(maze: MazeGenerator) -> None:
    """Permet de choisir le mode d'affichage du labyrinthe."""
    while True:
        print("\nChoose display mode:")
        print("[1] Terminal")
        print("[2] Pygame")

        choice = input("Choice: ").strip()

        if choice == "1":
            terminal_menu(maze)
            break
        elif choice == "2":
            run_pygame(maze)
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")


def main() -> None:
    """Point d'entree du programme."""
    if len(sys.argv) != 2:
        print("usage: python3 a_maze_ing.py config.txt", file=sys.stderr)
        sys.exit(1)
    try:
        file_config = sys.argv[1]
        dico_config = parse_config(file_config)
        maze_config = convert_config(dico_config)
        blocked = create_pattern42(maze_config.width, maze_config.height)

        maze = MazeGenerator(
            width=maze_config.width,
            height=maze_config.height,
            entry=maze_config.entry,
            exit=maze_config.exit,
            perfect=maze_config.perfect,
            seed=maze_config.seed,
            blocked=blocked
        )
        maze.generate()
        write_output(maze, maze_config.output_file)
        choose_display(maze)
    except ConfigError as e:
        print(f"Erreur : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
