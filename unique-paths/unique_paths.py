def isAtEnd(grid, row, col):
    return len(grid) - 1 == row and len(grid[row]) - 1 == col


def validSquare(grid, row, col):
    if row >= len(grid) or col >= len(grid[row]):
        return False
    return grid[row][col] == 1


# Runtime: O(2^n)
def count_paths_duplicate_work(grid, row, col):
    if not validSquare(grid, row, col):
        return 0
    if isAtEnd(grid, row, col):
        return 1
    return count_paths_duplicate_work(grid, row + 1, col) + count_paths_duplicate_work(grid, row, col + 1)


# Runtime: O(n^2)
def count_paths(grid, row, col, paths):
    if not validSquare(grid, row, col):
        return 0
    if isAtEnd(grid, row, col):
        return 1
    if paths[row][col] == 0:
        paths[row][col] = count_paths(grid, row + 1, col, paths) + count_paths(grid, row, col + 1, paths)
    return paths[row][col]


def unique_paths(grid):
    rows = len(grid)
    if rows <= 0:
        return 0
    cols = len(grid[0])
    paths = [[0] * cols for i in range(rows)]
    return count_paths(grid, 0, 0, paths)
