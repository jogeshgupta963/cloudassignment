import numpy as np
import time
from colorama import init, Fore, Back, Style

# Initialize colorama
init(autoreset=True)

# Constants
WIDTH, HEIGHT = 50, 50

# Function to initialize the grid with random live and dead cells
def initialize_grid():
    return np.random.choice([0, 1], size=(WIDTH, HEIGHT))

# Function to count the live neighbors of a cell
def count_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            new_x, new_y = x + i, y + j
            if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
                count += grid[new_x, new_y]
    return count

# Function to update the grid based on the rules
def update_grid(grid):
    new_grid = grid.copy()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            neighbors = count_neighbors(grid, x, y)
            if grid[x, y] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid

# Function to print the grid to the console with colors
def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 1:
                print(Back.GREEN + '  ', end='')
            else:
                print(Back.BLACK + '  ', end='')
        print(Style.RESET_ALL)

# Main function
def main():
    grid = initialize_grid()

    while True:
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(0.1)  # Adjust the speed of the simulation

if __name__ == "__main__":
    main()
