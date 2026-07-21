'''
Topological sort
'''
from collections import deque


def can_finish_dfs(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Returns True if all courses can be completed (no cycle).
    Uses DFS with 3-state visited tracking.
    """
    # Build adjacency list
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[course].append(prereq)  # course → prereq

    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * num_courses

    def has_cycle(course: int) -> bool:
        # If node is currently in recursion stack, we found a cycle
        if state[course] == 1:
            return True

        # If already fully processed, no cycle from here
        if state[course] == 2:
            return False

        # Mark as visiting
        state[course] = 1

        # Visit all prerequisites
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True

        # Mark as fully processed
        state[course] = 2
        return False

    # Check each course (graph might be disconnected)
    for course in range(num_courses):
        if state[course] == 0:
            if has_cycle(course):
                return False

    return True


def can_finish_bfs(num_courses: int, prerequisites: list[list[int]]) -> bool:
    """
    Returns True if all courses can be completed.
    Uses Kahn's algorithm (Topological Sort with BFS).
    """
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses

    for course, prereq in prerequisites:
        graph[prereq].append(course)  # prereq → course
        indegree[course] += 1

    # Initialize queue with courses that have no prerequisites
    queue = deque([i for i in range(num_courses) if indegree[i] == 0])

    # Process courses
    processed = 0
    while queue:
        course = queue.popleft()
        processed += 1

        for next_course in graph[course]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)

    # If all courses processed, no cycle
    return processed == num_courses


if __name__ == "__main__":
    NUM_COURSE = 2
    PREREQUISITES = [[1, 0], [0, 1]]
    print(can_finish_dfs(NUM_COURSE, PREREQUISITES))

    NUM_COURSE1 = 4
    PREREQUISITES1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(can_finish_dfs(NUM_COURSE1, PREREQUISITES1))

    print("----------------------------------------------------")
    print(can_finish_bfs(NUM_COURSE, PREREQUISITES))
    print(can_finish_bfs(NUM_COURSE1, PREREQUISITES1))
