import time
def is_valid_partial(grid, solution, n, row, col):
    # Check no adjacent black cells
    if solution[row][col] == 'B':
        if (row > 0 and solution[row-1][col] == 'B') or (row < n-1 and solution[row+1][col] == 'B') or \
           (col > 0 and solution[row][col-1] == 'B') or (col < n-1 and solution[row][col+1] == 'B'):
            return False

    # Check row uniqueness up to current cell
    row_nums = set()
    for j in range(n):
        if solution[row][j] == 'W':
            if grid[row][j] in row_nums:
                return False
            row_nums.add(grid[row][j])

    # Check column uniqueness up to current cell
    col_nums = set()
    for i in range(n):
        if solution[i][col] == 'W':
            if grid[i][col] in col_nums:
                return False
            col_nums.add(grid[i][col])

    return True

def is_connected(solution, n):
    visited = [[False]*n for _ in range(n)]
    start_found = False
    for i in range(n):
        for j in range(n):
            if solution[i][j] != 'B':
                start_x, start_y = i, j
                start_found = True
                break
        if start_found:
            break

    if not start_found:
        return True

    stack = [(start_x, start_y)]
    while stack:
        x, y = stack.pop()
        if visited[x][y]:
            continue
        visited[x][y] = True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and solution[nx][ny] != 'B':
                stack.append((nx, ny))

    for i in range(n):
        for j in range(n):
            if solution[i][j] != 'B' and not visited[i][j]:
                return False

    return True

def solve_hitori(grid, n, solution, row=0, col=0):
    if row == n:
        return is_connected(solution, n)
    
    if col == n:
        return solve_hitori(grid, n, solution, row + 1, 0)
    
    # Option 1: Leave the cell white
    solution[row][col] = 'W'
    if is_valid_partial(grid, solution, n, row, col) and solve_hitori(grid, n, solution, row, col + 1):
        return True
    
    # Option 2: Color the cell black
    solution[row][col] = 'B'
    if is_valid_partial(grid, solution, n, row, col) and solve_hitori(grid, n, solution, row, col + 1):
        return True
    
    # Backtrack
    solution[row][col] = '.'
    return False

def print_solution(solution, grid):
    for i in range(len(solution)):
        for j in range(len(solution[i])):
            print(grid[i][j] if solution[i][j] == 'W' else 'X', end=' ')
        print()

def main():
    grid = [
  [2, 7, 8, 3, 9, 10, 3, 5, 8, 9, 2, 1, 1, 12, 12],
  [6, 8, 5, 10, 1, 12, 4, 7, 14, 13, 14, 15, 11, 9, 5],
  [12, 9, 14, 2, 8, 6, 10, 10, 12, 7, 8, 4, 2, 11, 7],
  [4, 14, 11, 6, 14, 12, 12, 13, 2, 7, 7, 5, 2, 4, 6],
  [3, 2, 10, 4, 12, 13, 14, 15, 7, 11, 14, 13, 5, 1, 1],
  [2, 1, 1, 11, 8, 10, 3, 8, 10, 12, 12, 13, 7, 3, 11],
  [1, 1, 3, 14, 15, 3, 6, 9, 5, 13, 12, 8, 8, 15, 13],
  [1, 6, 9, 13, 10, 5, 5, 9, 8, 3, 6, 2, 14, 12, 14],
  [9, 9, 12, 10, 15, 5, 13, 8, 5, 10, 1, 2, 6, 4, 2],
  [8, 15, 11, 11, 6, 1, 10, 2, 2, 1, 5, 9, 15, 7, 6],
  [8, 14, 5, 9, 3, 1, 11, 2, 7, 6, 5, 7, 12, 8, 4],
  [15, 12, 6, 3, 2, 6, 14, 5, 9, 5, 7, 12, 7, 3, 2],
  [13, 12, 6, 6, 2, 11, 7, 3, 12, 8, 1, 1, 9, 2, 14],
  [7, 13, 3, 12, 9, 4, 6, 1, 11, 14, 6, 12, 15, 5, 11],
  [12, 8, 7, 12, 11, 4, 9, 14, 9, 4, 1, 3, 8, 13, 1]
]
    n = len(grid)
    solution = [['.' for _ in range(n)] for _ in range(n)]
    start_time = time.perf_counter()
    if solve_hitori(grid, n, solution):
        print("Solution found:")
        print_solution(solution, grid)
    else:
        print("No solution exists")

    end_time = time.perf_counter()
    execution_time = (end_time - start_time) * 1000 
    print(f"Execution time: {execution_time:.3f} milliseconds")


if __name__ == '__main__':
    main()
