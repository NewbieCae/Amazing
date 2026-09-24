from mazegen import MazeGenerator
from mazegen.pattern42 import create_pattern42
from collections import deque
from mazegen.generator import MOVES


def test_pacman_mode() -> None:
    for seed in range(100):
        blocked = create_pattern42(20, 15)
        maze = MazeGenerator(
            width=20,
            height=15,
            entry=(0, 0),
            exit=(19, 14),
            perfect=False,
            seed=seed,
            blocked=blocked
        )
        maze.generate()

        visited = {maze.entry}
        queue = deque([maze.entry])
        while queue:

            current = queue.popleft()
            x, y = current

            for direction in MOVES:
                if not maze.has_wall(x, y, direction):
                    dx, dy = MOVES[direction]
                    neighbor = (x + dx, y + dy)
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        dead_ends = 0
        for y in range(maze.height):
            for x in range(maze.width):
                if maze._open_count(x, y) == 1:
                    dead_ends += 1
        assert dead_ends <= 3
        assert maze._has_open_3x3() is False
        expected = maze.width * maze.height - len(blocked)
        assert len(visited) == expected
