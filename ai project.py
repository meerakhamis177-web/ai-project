from collections import deque

# The maze is represented as a 2D list
maze = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', 'S', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '#'],
    ['#', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', 'G', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]



def print_maze(maze):
    """Prints the maze row by row."""
    for row in maze:
        print(' '.join(row))


def find_position(maze, symbol):
    """Finds the position of S or G in the maze."""
    for row in range(len(maze)):
        for column in range(len(maze[row])):
            if maze[row][column] == symbol:
                return row, column

    return None


def solve_maze(maze):
    """Finds the shortest path using Breadth-First Search."""

    start = find_position(maze, 'S')
    goal = find_position(maze, 'G')

    # A queue is used by BFS
    queue = deque([start])

    # Stores the position visited before reaching each cell
    previous = {start: None}

    # Possible movements: up, down, left, right
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    # Continue searching while the queue is not empty
    while queue:
        current = queue.popleft()

        # Stop when the goal is reached
        if current == goal:
            break

        current_row, current_column = current

        # Check all four possible directions
        for row_change, column_change in directions:
            new_row = current_row + row_change
            new_column = current_column + column_change
            new_position = (new_row, new_column)

            # Check whether the new position is inside the maze
            inside_maze = (
                0 <= new_row < len(maze) and
                0 <= new_column < len(maze[0])
            )

            if not inside_maze:
                continue

            # Do not move through walls
            if maze[new_row][new_column] == '#':
                continue

            # Do not visit the same position more than once
            if new_position in previous:
                continue

            # Remember how we reached this position
            previous[new_position] = current

            # Add the new position to the queue
            queue.append(new_position)

    # If the goal was never visited, there is no solution
    if goal not in previous:
        return False, 0

    # Rebuild the path by moving backwards from G to S
    path = []
    current = goal

    while current is not None:
        path.append(current)
        current = previous[current]

    # The path was built backwards, so reverse it
    path.reverse()

    # Mark the path with '*'
    # Keep S and G unchanged
    for row, column in path[1:-1]:
        maze[row][column] = '*'

    # Path length means the number of movements
    path_length = len(path) - 1

    return True, path_length


# Display the original maze
print("Maze before solving:")
print_maze(maze)

# Solve the maze
solution_found, path_length = solve_maze(maze)

# Display the solved maze
print("\nMaze after solving:")
print_maze(maze)

# Display the result
if solution_found:
    print("\nSolution found!")
    print("Path length:", path_length)
else:
    print("\nNo solution was found.")