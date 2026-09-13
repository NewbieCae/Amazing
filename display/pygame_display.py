import pygame

SIZE_CELL = 50

def run_pygame(maze) -> None:
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("A-Maze-ing")

    running = True

    while running:
        screen.fill((30, 30, 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for y in range(maze.height):
            for x in range(maze.width):
                draw_cell(maze, screen, x, y)

        pygame.display.flip()


def draw_cell(maze, screen, x: int, y: int) -> None:
    pixel_x = x * SIZE_CELL
    pixel_y = y * SIZE_CELL

    if maze.has_wall(x, y, "N"):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (pixel_x, pixel_y),
            (pixel_x + SIZE_CELL, pixel_y),
            3,
        )
    if maze.has_wall(x, y, "E"):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (pixel_x + SIZE_CELL, pixel_y),
            (pixel_x + SIZE_CELL, pixel_y + SIZE_CELL),
            3
        )
    if maze.has_wall(x, y, "S"):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (pixel_x + SIZE_CELL, pixel_y + SIZE_CELL),
            (pixel_x, pixel_y + SIZE_CELL),
            3
        )
    if maze.has_wall(x, y, "S"):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (pixel_x, pixel_y + SIZE_CELL),
            (pixel_x, pixel_y),
            3
        )


if __name__ == "__main__":
    from mock_maze import MockMaze

    maze = MockMaze()
    run_pygame(maze)
