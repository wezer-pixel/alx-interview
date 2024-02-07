# N Queens Problem using Backtracking

The N Queens problem is a classic chessboard puzzle where the goal is to place N queens on an N×N chessboard in such a way that no two queens threaten each other. This implementation uses the backtracking algorithm to find a solution.

## Problem Description

The problem involves placing N queens on an N×N chessboard, ensuring that no two queens share the same row, column, or diagonal. The backtracking algorithm systematically explores possible placements until a valid solution is found or all possibilities are exhausted.

## Implementation Steps

Follow the steps below to implement the backtracking algorithm for the N Queens problem:

1. **Start in the leftmost column**: Begin placing queens one by one, starting from the leftmost column.

2. **Check if all queens are placed**: If all queens are successfully placed, return true as a solution has been found.

3. **Try all rows in the current column**: Iterate through each row in the current column and follow the steps below:

    a. If the queen can be placed safely in the current row, mark this [row, column] as part of the solution.

    b. Recursively try placing the queen in the next column.

    c. If placing the queen in [row, column] leads to a solution, return true.

    d. If placing the queen doesn't lead to a solution, backtrack by undoing the marking of [row, column].

4. **If all rows have been tried**: If all rows in the current column have been tried and no valid solution is found, return false.

## How to Use

To use the implementation:

```python
from n_queens import solve_n_queens

# Specify the size of the chessboard (N)
n = 8  # For an 8x8 chessboard

# Call the solve_n_queens function
solution = solve_n_queens(n)

if solution:
    print(f"Solution for {n} Queens problem:\n{solution}")
else:
    print(f"No solution found for {n} Queens problem.")
```

This implementation provides a clear and concise solution to the N Queens problem using the backtracking algorithm. 
Feel free to customize the code according to your needs. 
