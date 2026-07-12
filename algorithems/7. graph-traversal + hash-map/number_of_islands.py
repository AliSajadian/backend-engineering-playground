'''
number_of_islands.py
'''
from collections import deque


def num_islands_dfs(grid: list[list[str]]) -> int:
    """
    Returns number of islands in the grid using DFS.
    Modifies grid in-place to mark visited cells.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r: int, c: int):
        """Explore all connected land cells from (r, c)"""
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return

        grid[r][c] = "0"

        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c  + 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)

    return islands


def num_islands_bfs(grid: list[list[str]]) -> int:
    '''
    Returns number of islands in the grid using DFS.
    Modifies grid in-place to mark visited cells.
    '''
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    islands = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                grid[r][c] = '0'  # Mark visited
                queue = deque([(r, c)])

                while queue:
                    curr_r, curr_c = queue.popleft()

                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc

                        # Check bounds and if it's unvisited land
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1':
                            grid[nr][nc] = '0'  # Mark visited
                            queue.append((nr, nc))

    return islands


if __name__ == "__main__":
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(num_islands_dfs(grid1))

    grid2 = [
        ["1","1","1","0","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    print(num_islands_dfs(grid2))

    grid3 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(num_islands_dfs(grid3))
