
PATTERN_WIDTH = 7
PATTERN_HEIGHT = 5

def create_pattern42(width: int, height: int) -> set[tuple[int, int]]:
    if width < PATTERN_WIDTH or height < PATTERN_HEIGHT:
        print("The motif doesn't enter")
        return set()
        

    offset_x = width // 2 - 3
    offset_y = (height - PATTERN_HEIGHT) // 2

    pattern = set()

    local_cells = [
        (0,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2), (2,3), (2,4),(4,0),
        (5,0), (6,0), (6,1), (4,2), (5,2), (6,2), (4,3), (4,4),(5,4),(6,4)
    ]

    for local_x, local_y in local_cells:
        pattern.add((local_x + offset_x, local_y + offset_y))

    return pattern
