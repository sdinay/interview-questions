# Unique Paths with Obstacles

Matrix unique paths with obstacles question

## Question

Find all unique paths from the top left corner (0, 0) to the bottom right corner (n, m) of a matrix. Each spot in the matrix has either a value of 0 or 1. A path can only cross through a spot marked with a 1 and each move can only be made in the down or right direction.

Example:
```
 +---+---+---+---+---+
 | 1 | 1 | 0 | 1 | 1 |
 +---+---+---+---+---+
 | 0 | 1 | 1 | 1 | 1 |
 +---+---+---+---+---+
 | 0 | 1 | 1 | 0 | 1 |
 +---+---+---+---+---+
 | 1 | 1 | 1 | 1 | 1 |
 +---+---+---+---+---+
```

This board has 4 unique paths and you can test this by running `pytest`

## Install and Test

### Python

```
pip install --upgrade pip
pip install -r requirements.txt
pytest -s
```

## Maintainer

https://github.com/sdinay

## References

https://youtu.be/P8Xa2BitN3I

https://leetcode.com/problems/unique-paths/
