def READ_GRID(FILE_NAME):
    with open(FILE_NAME, 'r') as file:
        return [list(line.strip()) for line in file]

def IS_VALID_POS(GRID, ROW, COL):
    return 0 <= ROW < len(GRID) and 0 <= COL < len(GRID[0])

def IS_VALID_MAS_POS(X, Y, MAX_X, MAX_Y):
    if X < 0 or X >= MAX_X or Y < 0 or Y >= MAX_Y:
        return False
    return True

def DIRECTIONS():
    return [
        (0, 1),   # right
        (1, 1),   # down-right
        (1, 0),   # down
        (1, -1),  # down-left
        (0, -1),  # left
        (-1, -1), # up-left
        (-1, 0),  # up
        (-1, 1)   # up-right
    ]

def FOUND_MAS(X, Y, PATTERN, GRID):
    for char, dx, dy in PATTERN:
        new_x, new_y = X + dx, Y + dy

        if not IS_VALID_MAS_POS(new_x, new_y, len(GRID), len(GRID[0])):
            return False

        if GRID[new_x][new_y] != char:
            return False
    return True

def FIND_MAS(GRID):
    COUNT = 0
    MAS_DIRECTIONS = [
        [('M', -1, -1), ('S', -1, 1), ('A', 0, 0), ('M', 1, -1), ('S', 1, 1)],  # Rotated 0
        [('S', -1, -1), ('M', 1, -1), ('A', 0, 0), ('S', -1, 1), ('M', 1, 1)],  # Rotated 90
        [('S', 1, -1), ('M', 1, 1), ('A', 0, 0), ('S', -1, -1), ('M', -1, 1)],  # Rotated 180
        [('M', -1, 1), ('S', 1, 1), ('A', 0, 0), ('M', -1, -1), ('S', 1, -1)]  # Rotated 270
    ]

    # Iterate through grid
    for x in range(len(GRID)):
        for y in range(len(GRID[0])):
            for PATTERN in MAS_DIRECTIONS:
                if FOUND_MAS(x, y, PATTERN, GRID):
                    COUNT += 1

    return COUNT

def FIND_XMAS(GRID):
    XMAS_COUNT = 0
    ROWS, COLS = len(GRID), len(GRID[0])
    TARGET = list("XMAS")

    for START_ROW in range(ROWS):
        for START_COL in range(COLS):
            for dx, dy in DIRECTIONS():
                # Check if the entire word can be found starting from this position
                FOUND = True
                for step in range(4):
                    ROW = START_ROW + step * dx
                    COL = START_COL + step * dy
                    
                    # Check if current position is valid and matches the target letter
                    if (not IS_VALID_POS(GRID, ROW, COL) or 
                        GRID[ROW][COL] != TARGET[step]):
                        FOUND = False
                        break
                
                # If found, increment count
                if FOUND:
                    XMAS_COUNT += 1

    return XMAS_COUNT

def main():
    GRID = READ_GRID('Advent-of-Code-2024/Day 4/dataset.txt')

    RESULT = FIND_XMAS(GRID)
    MAS_RESULT = FIND_MAS(GRID)

    print("Part 1:", RESULT)
    print("Part 2:", MAS_RESULT)

if __name__ == "__main__":
    main()