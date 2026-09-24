from mazegen import MazeGenerator
from mazegen.pattern42 import create_pattern42
from mazegen.generator import MOVES


def test_pattern42_closed_cells() -> None:
    for seed in range(100):
        blocked = create_pattern42(20, 15)
        assert len(blocked) == 20
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

        for x, y in blocked:
            for direction in MOVES:
                assert maze.has_wall(x, y, direction) is True


def test_pattern42_too_small() -> None:
    small_pattern = create_pattern42(5, 4)
    assert small_pattern == set()
