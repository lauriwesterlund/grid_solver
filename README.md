# grid_solver
Solves an old number placement puzzle.

![Illustration of a solved grid puzzle](https://github.com/lauriwesterlund/grid_solver/blob/main/grid_solution.png)

The classic variant involves a 10x10 grid. The numbers 1 to 100 are placed in the grid in ascending order.
- The first number can be placed in any cell.
- Subsequent numbers must be placed in an unoccupied cell that is either 3 cells away from the previous number horizontally or vertically, or 2 cells away diagonally.
- The numbers cannot be wrapped around the boundaries.

The goal is to finish with the grid completely filled with all the numbers, or to reach the highest number possible.

This script attempts to solve the puzzle from a given starting position. Grid size can be altered. It uses heuristic-based move sorting and depth-first search with backtracking to find the solution as efficiently as possible.

The script finds the solution for most starting points in a couple of seconds, and quickly finds a solution that reaches 98-99 for all of them. I suspect the puzzle is solvable from any starting point, but finding those solutions would take too long.
