import pygame
from mazegen.pattern42 import create_pattern42
from mazegen import MazeGenerator

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def draw_cell(
        maze: MazeGenerator,
        screen: pygame.Surface,
        x: int,
        y: int,
        offset_x: int,
        offset_y: int,
        cell_size: int,
        wall_color: tuple[int, int, int],
        pattern_color: tuple[int, int, int],
        ) -> None:

    pixel_x = offset_x + x * cell_size
    pixel_y = offset_y + y * cell_size

    if (x, y) in maze.blocked:
        pygame.draw.rect(screen, pattern_color, (pixel_x, pixel_y, cell_size,
                                                 cell_size))

    if maze.has_wall(x, y, "N"):
        pygame.draw.line(screen, wall_color, (pixel_x, pixel_y),
                         (pixel_x + cell_size, pixel_y), 3)
    if maze.has_wall(x, y, "E"):
        pygame.draw.line(screen, wall_color, (pixel_x + cell_size, pixel_y),
                                             (pixel_x + cell_size, pixel_y
                                              + cell_size), 3)
    if maze.has_wall(x, y, "S"):
        pygame.draw.line(screen, wall_color, (pixel_x + cell_size,
                                              pixel_y + cell_size),
                                             (pixel_x, pixel_y + cell_size), 3)
    if maze.has_wall(x, y, "W"):
        pygame.draw.line(screen, wall_color, (pixel_x, pixel_y + cell_size),
                                             (pixel_x, pixel_y), 3)


def draw_entry_exit(maze: MazeGenerator,
                    screen: pygame.Surface,
                    offset_x: int,
                    offset_y: int,
                    cell_size: int,
                    entry_color: tuple[int, int, int],
                    exit_color: tuple[int, int, int]) -> None:

    maze_entry_x, maze_entry_y = maze.entry  # tuple unpacking
    maze_exit_x, maze_exit_y = maze.exit

    entry_pixel_x = offset_x + maze_entry_x * cell_size
    entry_pixel_y = offset_y + maze_entry_y * cell_size

    exit_pixel_x = offset_x + maze_exit_x * cell_size
    exit_pixel_y = offset_y + maze_exit_y * cell_size

    entry_center_pixel_x = entry_pixel_x + cell_size // 2
    entry_center_pixel_y = entry_pixel_y + cell_size // 2

    exit_center_pixel_x = exit_pixel_x + cell_size // 2
    exit_center_pixel_y = exit_pixel_y + cell_size // 2

    font = pygame.font.Font(None, 30)

    entry_text = font.render("S", True, entry_color)
    exit_text = font.render("E", True, exit_color)

    entry_rect = entry_text.get_rect(center=(entry_center_pixel_x,
                                             entry_center_pixel_y))
    exit_rect = exit_text.get_rect(center=(exit_center_pixel_x,
                                           exit_center_pixel_y))

    screen.blit(entry_text, entry_rect)
    screen.blit(exit_text, exit_rect)


def draw_path(maze: MazeGenerator,
              screen: pygame.Surface,
              offset_x: int,
              offset_y: int,
              cell_size: int,
              path_color: tuple[int, int, int]) -> None:
    path = maze.find_path()

    if path:
        previous_point = None

        for path_x, path_y in path:
            path_pixel_x = offset_x + path_x * cell_size
            path_pixel_y = offset_y + path_y * cell_size

            path_center_pixel_x = path_pixel_x + cell_size // 2
            path_center_pixel_y = path_pixel_y + cell_size // 2

            current_point = (path_center_pixel_x, path_center_pixel_y)
            if previous_point is not None:
                pygame.draw.line(
                    screen,
                    path_color,
                    previous_point,
                    current_point,
                    3
                )
            previous_point = current_point


def draw_interface(
        screen: pygame.Surface,
        wall_color: tuple[int, int, int],
        pattern_color: tuple[int, int, int],
        show_path: bool
        ) -> None:

    title_font = pygame.font.Font(None, 36)
    control_font = pygame.font.Font(None, 22)

    title = title_font.render(
        "A-MAZE-ING // 42",
        True,
        wall_color
    )

    title_rect = title.get_rect(
        center=(SCREEN_WIDTH // 2, 30)
    )

    screen.blit(title, title_rect)

    path_status = "ON" if show_path else "OFF"
    controls_keys = (
        f"[P] PATH: {path_status}   "
        "[R] REGENERATE    "
        "[C] COLOR    "
        "[Q] QUIT"
        )

    controls_text = control_font.render(
        controls_keys,
        True,
        pattern_color
    )

    controls_rect = controls_text.get_rect(
        center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 35)
    )

    screen.blit(controls_text, controls_rect)


def run_pygame(maze: MazeGenerator) -> None:
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    max_cell_size = 50
    header_height = 60
    footer_height = 60

    available_height = SCREEN_HEIGHT - header_height - footer_height

    cell_width = SCREEN_WIDTH // maze.width
    cell_height = available_height // maze.height

    cell_size = min(cell_width, cell_height, max_cell_size)

    maze_pixel_width = maze.width * cell_size
    maze_pixel_height = maze.height * cell_size

    offset_x = (SCREEN_WIDTH - maze_pixel_width) // 2
    offset_y = header_height + (available_height - maze_pixel_height) // 2

    pygame.display.set_caption("A-Maze-ing")

    running = True
    show_path = False
    background_color = (8, 10, 15)

    pattern_color = (255, 46, 136)
    path_color = (249, 248, 113)

    entry_color = (0, 255, 133)
    exit_color = (255, 59, 92)

    wall_colors = [
        (0, 245, 212),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
    ]

    wall_color_index = 0
    wall_color = wall_colors[wall_color_index]

    while running:
        screen.fill(background_color)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    show_path = not show_path
                elif event.key == pygame.K_r:
                    maze.generate()
                elif event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_c:
                    wall_color_index = (wall_color_index + 1) % len(wall_colors)
                    wall_color = wall_colors[wall_color_index]

        for y in range(maze.height):
            for x in range(maze.width):
                draw_cell(maze,
                          screen,
                          x,
                          y,
                          offset_x,
                          offset_y, cell_size, wall_color, pattern_color)

        if show_path:
            draw_path(maze,
                      screen,
                      offset_x,
                      offset_y,
                      cell_size,
                      path_color)

        draw_entry_exit(
            maze,
            screen,
            offset_x,
            offset_y,
            cell_size,
            entry_color,
            exit_color,
        )

        draw_interface(
            screen,
            wall_color,
            pattern_color,
            show_path
        )

        pygame.display.flip()


if __name__ == "__main__":

    blocked = create_pattern42(20, 15)
    maze = MazeGenerator(
        width=20,
        height=15,
        entry=(0, 0),
        exit=(19, 14),
        perfect=True,
        seed=42,
        blocked=blocked
    )
    maze.generate()
    run_pygame(maze)
