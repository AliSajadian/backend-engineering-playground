'''
    Grid BFS
'''
from collections import deque

def oranges_rotting(grid: list[list[int]]) -> int:
    '''
    Orange rotting
    '''
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Initialize: find all rotten oranges and count fresh
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    if fresh == 0:
        return 0

    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # BFS level by level
    while queue and fresh > 0:
        multi_source__bfs_level_size = len(queue)
        for _ in range(multi_source__bfs_level_size):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))

        minutes += 1

    return minutes if fresh == 0 else -1


# Test
if __name__ == "__main__":
    grid1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    print(oranges_rotting(grid1))  # Output: 4

    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]


    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    print(graph)
