# Lockboxes

## Description

You are given `n` number of locked boxes, each numbered sequentially from 0 to n - 1. Each box may contain keys to other boxes, and a key with the same number as a box can open that box. The first box `boxes[0]` is initially unlocked. The task is to implement a Python method to determine if all the boxes can be opened.

## Method Signature

```python
def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists where each list represents a box and contains positive integers as keys.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    pass
```

## Examples

### Example 1

```python
# Example 1
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True
```

### Example 2

```python
# Example 2
boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True
```

### Example 3

```python
# Example 3
boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
```

## Approach

The method uses a set to keep track of opened boxes and a queue to store the keys that need to be checked. It iteratively explores the keys until there are no more keys to check, and at the end, it checks if the number of opened boxes is equal to the total number of boxes.

## How to Use

1. Clone the repository.
2. Import the `canUnlockAll` method from the `lockboxes` module.
3. Create a list of lists representing the locked boxes.
4. Call the `canUnlockAll` method with the list of boxes as an argument.

```python
from lockboxes import canUnlockAll

# Example usage
boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))  # Output: True
```

