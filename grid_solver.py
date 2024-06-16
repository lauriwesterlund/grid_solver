# Version: 1.0
# Author: Lauri Westerlund
# Date: 2024-06-16
#
# This is a Python script that solves an old number placement puzzle on a grid.
# The goal is to place numbers from 1 to N^2 on an NxN grid such that each number is placed in a cell
# that is exactly 3 cells away horizontally or vertically) or 2 cells away diagonally from the previous
# number.

import numpy as np
import os
import time

# Initialize the grid size
GRID_SIZE = 10

# Defines movement constraints
def is_valid_move(grid, x, y):
    # Check boundaries
    if x < 0 or x >= GRID_SIZE or y < 0 or y >= GRID_SIZE:
        return False
    # Check if the cell is already occupied
    if grid[x, y] != 0:
        return False
    return True

# Gets valid moves from a given position
def get_valid_moves(x, y):
    return [
        (x + 3, y), (x - 3, y),
        (x, y + 3), (x, y - 3),
        (x + 2, y + 2), (x - 2, y - 2),
        (x + 2, y - 2), (x - 2, y + 2)
    ]

# Clears the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Prints the grid and other information
def print_grid(grid, dead_ends, highest_number, current_number, x, y, start_time):
    clear_console()
    elapsed_time = time.time() - start_time
    print(f"Placing number: {current_number} at position: ({x}, {y})")
    print(f"Dead ends: {dead_ends[0]}")
    print(f"Highest number reached so far: {highest_number[0]}")
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print("Current grid state:")
    print(grid)
    # time.sleep(0.1)  # Pause to better visualize the changes

# Heuristic to sort valid moves based on the number of subsequent moves
def sort_moves_by_constraint(grid, moves):
    move_constraints = []
    for move in moves:
        x, y = move
        count = sum(1 for dx, dy in get_valid_moves(x, y) if is_valid_move(grid, dx, dy))
        move_constraints.append((count, move))
    move_constraints.sort()
    return [move for count, move in move_constraints]

# Solves the grid from a given position
def solve(grid, x, y, current_number, dead_ends, highest_number, start_time):
    # Check if the grid is solved
    if current_number > GRID_SIZE * GRID_SIZE:
        return True

    # Get valid moves and sort them by constraint
    valid_moves = [move for move in get_valid_moves(x, y) if is_valid_move(grid, move[0], move[1])]
    sorted_moves = sort_moves_by_constraint(grid, valid_moves)

    # Try each valid move
    for dx, dy in sorted_moves:
        # Place the number
        grid[dx, dy] = current_number
        # Update the highest number reached so far and store the best solution
        if current_number > highest_number[0]:
            highest_number[0] = current_number
            highest_number[1] = grid.copy()
        # Print the grid and other information
        print_grid(grid, dead_ends, highest_number, current_number, dx, dy, start_time)
        # Recursively solve the grid
        if solve(grid, dx, dy, current_number + 1, dead_ends, highest_number, start_time):
            return True
        # Backtracking if no solution found
        grid[dx, dy] = 0
        dead_ends[0] += 1
        print_grid(grid, dead_ends, highest_number, current_number - 1, dx, dy, start_time)

    return False

def solve_grid_from_starting_position(starting_x ,starting_y):
    dead_ends = [0]
    highest_number = [0, np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)]
    start_time = time.time()
    try:
        grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        grid[starting_x, starting_y] = 1
        print_grid(grid, dead_ends, highest_number, 1, starting_x, starting_y, start_time)
        if solve(grid, starting_x, starting_y, 2, dead_ends, highest_number, start_time):
            elapsed_time = time.time() - start_time
            clear_console()
            print("Solution found when starting from ({}, {}) after {} dead ends in {:.2f} seconds:".format(starting_x, starting_y, dead_ends[0], elapsed_time))
            print(highest_number[1])
        else:
            elapsed_time = time.time() - start_time
            elapsed_time = time.time() - start_time
            clear_console()
            print("No solution found.")
            print("Total time: {:.2f} seconds".format(elapsed_time))
            print("Best solution:")
            print(highest_number[1])
    except KeyboardInterrupt:
        elapsed_time = time.time() - start_time
        clear_console()
        print("Interrupted by user.")
        print("Final state:")
        print(grid)
        print(f"Dead ends: {dead_ends[0]}")
        print("Elapsed time: {:.2f} seconds".format(elapsed_time))
        print(f"Highest number placed was {highest_number[0]}. The best solution found was:")
        print(highest_number[1])

def main():
    x, y = 0, 0

    while True:
        try:
            x = int(input(f"Enter the x coordinate (0 - {GRID_SIZE - 1}): "))
            if x >= 0 and x < GRID_SIZE:
                break
        except ValueError:
            pass

    while True:
        try:
            y = int(input(f"Enter the y coordinate (0 - {GRID_SIZE - 1}): "))
            if y >= 0 and y < GRID_SIZE:
                break
        except ValueError:
            pass

    solve_grid_from_starting_position(x, y)

if __name__ == "__main__":
    main()
