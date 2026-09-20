import random
from collections import deque
Cell = tuple[int, int]

MOVES = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}

BITS = {
    "N": 1,
    "E": 2,
    "S": 4,
    "W": 8,
}


def cell_sorter(first: Cell, second: Cell) -> tuple[Cell, Cell]:
    """Renvoie les deux cellules dans le bonne ordre."""
    if first < second:
        return (first, second)
    return (second, first)


class MazeGenerator:
    """Generateur de labyrinthe."""

    def __init__(
            self,
            width: int,
            height: int,
            entry: Cell,
            exit: Cell,
            perfect: bool = False,
            seed: int | None = None,
            blocked: set[Cell] | None = None,
            ) -> None:
        """Initialise le generateur avec les dimensions et les parametres."""
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        self.blocked = blocked if blocked is not None else set()
        self._passages: set[tuple[Cell, Cell]] = set()
        self._rng = random.Random(seed)

    def has_wall(self, x: int, y: int, direction: str) -> bool:
        """Indique s'il y a un mur dans cette direction."""
        dx, dy = MOVES[direction]
        vx, vy = x + dx, y + dy
        if vx < 0 or vx >= self.width or vy < 0 or vy >= self.height:
            return True
        passage = cell_sorter((x, y), (vx, vy))
        return passage not in self._passages

    def _neighbors(self, cell: Cell, visited: set[Cell]) -> list[Cell]:
        """Renvoie les voisines non visitees et accessibles d'une cellule."""
        res: list[Cell] = []
        x, y = cell
        for direction in MOVES:
            dx, dy = MOVES[direction]
            vx, vy = x + dx, y + dy
            if vx < 0 or vx >= self.width or vy < 0 or vy >= self.height:
                continue
            if (vx, vy) in visited:
                continue
            if (vx, vy) in self.blocked:
                continue
            res.append((vx, vy))
        return res

    def generate(self, seed: int | None = None) -> None:
        """Genere un nouveau labyrinthe."""
        if seed is not None:
            self.seed = seed
            self._rng = random.Random(seed)
        self._passages = set()
        depart = self.entry
        visited: set[Cell] = {depart}
        pile: list[Cell] = [depart]
        while pile:
            sommet = pile[-1]
            voisines = self._neighbors(sommet, visited)

            if not voisines:
                pile.pop()
                continue

            choisie = self._rng.choice(voisines)
            self._passages.add(cell_sorter(sommet, choisie))
            visited.add(choisie)
            pile.append(choisie)
        if not self.perfect:
            self._braid()
            self._open_special_cells()

    def find_path(self) -> list[Cell] | None:
        """renvoyer le plus court chemin de l'entrée à la sortie."""
        file: deque[Cell] = deque([self.entry])
        vues: set[Cell] = {self.entry}
        parents: dict[Cell, Cell] = {}
        while file:
            courante = file.popleft()
            if courante == self.exit:
                break
            x, y = courante
            for direction in MOVES:
                if not self.has_wall(x, y, direction):
                    dx, dy = MOVES[direction]
                    voisine = (x + dx, y + dy)
                    if voisine not in vues:
                        vues.add(voisine)
                        parents[voisine] = courante
                        file.append(voisine)
        if self.exit not in vues:
            return None
        chemin: list[Cell] = []
        courante = self.exit

        while courante != self.entry:
            chemin.append(courante)
            courante = parents[courante]
        chemin.append(self.entry)
        chemin.reverse()
        return chemin

    def to_grid(self) -> list[list[int]]:
        """Convertit le labyrinthe en grille de masques hexadecimaux."""
        grille: list[list[int]] = []
        for y in range(self.height):
            ligne: list[int] = []
            for x in range(self.width):
                mask = 0
                for direction in MOVES:
                    if self.has_wall(x, y, direction):
                        mask |= BITS[direction]
                ligne.append(mask)
            grille.append(ligne)
        return grille

    def _open_count(self, x: int, y: int) -> int:
        """Compte le nombre d'ouvertures d'une cellule."""
        count = 0
        for direction in MOVES:
            if not self.has_wall(x, y, direction):
                count += 1
        return count

    def _braid(self) -> None:
        """Ouvre des murs supplementaires pour supprimer les culs-de-sac."""
        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.blocked:
                    continue
                if self._open_count(x, y) == 1:
                    res: list[Cell] = []
                    for direction in MOVES:
                        dx, dy = MOVES[direction]
                        vx, vy = x + dx, y + dy
                        if (vx < 0 or vx >= self.width
                                or vy < 0 or vy >= self.height):
                            continue
                        if not self.has_wall(x, y, direction):
                            continue
                        if (vx, vy) in self.blocked:
                            continue
                        res.append((vx, vy))
                    if res:
                        choisie = self._rng.choice(res)
                        passage = cell_sorter((x, y), choisie)
                        self._passages.add(passage)
                        if self._has_open_3x3():
                            self._passages.discard(passage)

    def _is_open_3x3(self, x: int, y: int) -> bool:
        """Indique si le bloc 3x3 a ce coin est entierement ouvert."""
        for dy in range(3):
            for dx in range(3):
                cx, cy = x + dx, y + dy
                if dx < 2 and self.has_wall(cx, cy, "E"):
                    return False
                if dy < 2 and self.has_wall(cx, cy, "S"):
                    return False
        return True

    def _has_open_3x3(self) -> bool:
        """Indique s'il existe une zone ouverte 3x3 dans le labyrinthe."""
        for y in range(self.height - 2):
            for x in range(self.width - 2):
                if self._is_open_3x3(x, y):
                    return True
        return False

    def _open_special_cells(self) -> None:
        """Ouvre les quatre coins et le centre pour le mode Pac-Man."""
        specials = [
            (0, 0),
            (self.width - 1, 0),
            (0, self.height - 1),
            (self.width - 1, self.height - 1),
            (self.width // 2, self.height // 2),
        ]
        for x, y in specials:
            if self._open_count(x, y) < 2:
                res: list[Cell] = []
                for direction in MOVES:
                    dx, dy = MOVES[direction]
                    vx, vy = x + dx, y + dy
                    if (vx < 0 or vx >= self.width
                            or vy < 0 or vy >= self.height):
                        continue
                    if not self.has_wall(x, y, direction):
                        continue
                    if (vx, vy) in self.blocked:
                        continue
                    res.append((vx, vy))
                if res:
                    choisie = self._rng.choice(res)
                    passage = cell_sorter((x, y), choisie)
                    self._passages.add(passage)
                    if self._has_open_3x3():
                        self._passages.discard(passage)
