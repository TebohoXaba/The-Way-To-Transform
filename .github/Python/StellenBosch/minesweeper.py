# Create helper function to count adjacent ("-") mines
    # Where rows equal length of grid
    # And columns equal first index in the length of grid
    # Create variable to store the count (mine_count
def count_mines(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    mine_count = 0
    
    # Check all 8 directions around the current cell
    # Create a variable to store directions
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    # Use a for loop where for every row (dr) and column (dc) in the variable 'directions'
        # New row and column variables equal the row or column variables defined in the count of mines...
        # ... plus (+) loop values dr and dc
        # Using an if statement, check index values are not the symbol '#'
        # Program should increase mine count and value shown in grid by 1
    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == "#":
            mine_count += 1
    
    # return mine count (mine_count) in string format
    return str(mine_count)

# Create function called the minesweeper() to replace '-' with count of adjacent mines
    # Store updated grid as new_grid
def minesweeper(grid):
    new_grid = []
    
    # Using a for loop where if row in the range of the length of the grid
        # The variable new_row should be updated with a nested for loop
        # Where if the row and column indexes contain an adjacent
        # the new row must be appended using the count_mines() function
    for row in range(len(grid)):
        new_row = []
        for col in range(len(grid[0])):
            if grid[row][col] == "-":
                new_row.append(count_mines(grid, row, col))

            # Or else if not true, append/ keep new_row/ mines as '#'
            else:
                new_row.append("#")
        
        # Add updated row to new grid
        new_grid.append(new_row)
    
    # Return new_grid 2D list
    return new_grid

# Sample input grid (Compulsory task grid)
grid_input = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Run the function
result = minesweeper(grid_input)

# Print formatted output
for row in result:
    print(row)

'''This was hard!!'''