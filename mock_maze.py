class MockMaze:
    def __init__(self) -> None:
        self.width = 4
        self.height = 3
        self.entry = (0, 0)
        self.exit = (3, 2)

        self._walls = {
        # Bordure du haut
        (0, 0, "N"),
        (1, 0, "N"),
        (2, 0, "N"),
        (3, 0, "N"),

        # Bordure gauche
        (0, 0, "W"),
        (0, 1, "W"),
        (0, 2, "W"),

        # Murs verticaux internes / droite
        (0, 0, "E"),
        (1, 0, "E"),
        (3, 0, "E"),

        (2, 1, "E"),
        (3, 1, "E"),

        (1, 2, "E"),
        (3, 2, "E"),

        # Quelques murs horizontaux internes
        (0, 1, "N"),
        (2, 1, "N"),
        (1, 2, "N"),
        (3, 2, "N"),

        # Bordure du bas
        (0, 2, "S"),
        (1, 2, "S"),
        (2, 2, "S"),
        (3, 2, "S"),
    }

    def has_wall(self, x: int, y: int, direction: str) -> bool:
        return (x, y, direction) in self._walls

    def find_path(self) -> list[tuple[int, int]]:
        return [
            (0, 0),
            (1, 0),
            (1, 1),
            (2, 1),
            (2, 2),
            (3, 2),
        ]

    def generate(self, seed=None) -> None:
        pass