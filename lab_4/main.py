from collections import deque


def read_input(filename):
    with open(filename, 'r') as file:
        start = tuple(map(int, file.readline().strip().split(', ')))
        end = tuple(map(int, file.readline().strip().split(', ')))
        rows, cols = map(int, file.readline().strip().split(', '))
        grid = []
        for _ in range(rows):
            row = list(map(int, file.readline().strip().split()))
            grid.append(row)
    return start, end, grid


def find_shortest_path(start, end, grid):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, 0)])

    while queue:
        (x, y), distance = queue.popleft()

        if (x, y) == end:
            return distance

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x = x + dx
            new_y = y + dy
            if grid[new_x][new_y] == 1 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                queue.append(((new_x, new_y), distance + 1))

    return -1


start, end, grid = read_input('input.txt')
shortest_path = find_shortest_path(start, end, grid)
print(shortest_path)
