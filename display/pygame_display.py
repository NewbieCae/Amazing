import pygame


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def run_pygame(maze) -> None:
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    max_cell_size = 50

    cell_width = SCREEN_WIDTH // maze.width
    cell_height = SCREEN_HEIGHT // maze.height

    cell_size = min(cell_width, cell_height, max_cell_size)

    maze_pixel_width = maze.width * cell_size
    maze_pixel_height = maze.height * cell_size

    offset_x = (SCREEN_WIDTH - maze_pixel_width) // 2
    offset_y = (SCREEN_HEIGHT - maze_pixel_height) // 2

    pygame.display.set_caption("A-Maze-ing")

    running = True
    show_path = False

    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    show_path = not show_path
                elif event.key == pygame.K_r:
                    maze.generate()
                    print("regenerate r")
                elif event.key == pygame.K_q:
                    running = False
                    print("regenerate q")

        for y in range(maze.height):
            for x in range(maze.width):
                draw_cell(maze, screen, x, y, offset_x, offset_y, cell_size)

        if show_path:
            draw_path(maze, screen, offset_x, offset_y, cell_size)

        draw_entry_exit(maze, screen, offset_x, offset_y, cell_size)

        pygame.display.flip()


def draw_cell(
        maze, 
        screen, 
        x: int, y: int, offset_x: int, offset_y: int, cell_size: int)-> None:

    pixel_x = offset_x + x * cell_size
    pixel_y = offset_y + y * cell_size

    if maze.has_wall(x, y, "N"):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (pixel_x, pixel_y),
            (pixel_x + cell_size, pixel_y),
            3,
        )
    if maze.has_wall(x, y, "E"):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (pixel_x + cell_size, pixel_y),
            (pixel_x + cell_size, pixel_y + cell_size),
            3
        )
    if maze.has_wall(x, y, "S"):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (pixel_x + cell_size, pixel_y + cell_size),
            (pixel_x, pixel_y + cell_size),
            3
        )
    if maze.has_wall(x, y, "W"):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (pixel_x, pixel_y + cell_size),
            (pixel_x, pixel_y),
            3
        )


def draw_entry_exit(maze, 
                    screen, 
                    offset_x: int, offset_y: int, cell_size: int) -> None:

    maze_entry_x , maze_entry_y = maze.entry # tuple unpacking
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

    entry_text = font.render("E", True, (255, 255, 255))
    exit_text = font.render("S", True, (255, 255, 255))

    entry_rect = entry_text.get_rect(center=(entry_center_pixel_x, entry_center_pixel_y))
    exit_rect = exit_text.get_rect(center=(exit_center_pixel_x, exit_center_pixel_y))

    screen.blit(entry_text, entry_rect)
    screen.blit(exit_text, exit_rect)


def draw_path(maze, screen, offset_x: int, offset_y: int, cell_size: int) -> None:
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
                    (255, 255, 255),
                    previous_point,
                    current_point,
                    3
                )
            previous_point = current_point


if __name__ == "__main__":
    from mazegen import MazeGenerator

    maze = MazeGenerator(
    width=20,
    height=15,
    entry=(0, 0),
    exit=(19, 14),
    perfect=True,
    seed=42
)
    maze.generate()
    run_pygame(maze)
