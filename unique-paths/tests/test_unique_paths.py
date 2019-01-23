from unique_paths import unique_paths


def test_empty_grid():
    grid = []
    result = unique_paths(grid)
    assert result == 0

def test_readme_ex():
     grid = [
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1],
        [0, 1, 1, 0, 1],
        [1, 1, 1, 1, 1]
     ]
     result = unique_paths(grid)
     assert result == 4


def test_no_paths():
    grid = [
        [1, 0, 1],
        [1, 0, 1],
        [0, 1, 1]
    ]
    result = unique_paths(grid)
    assert result == 0


def test_zero_start():
    grid = [
        [0, 1, 1],
        [1, 1, 1]
    ]
    result = unique_paths(grid)
    assert result == 0


def test_all_ones():
    grid = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    result = unique_paths(grid)
    assert result == 6
