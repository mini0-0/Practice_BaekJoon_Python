import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

path = [(-1, 0), (1, 0), (0, 1), (0, -1)]
empty = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]
wall_combs = list(combinations(empty, 3))

def bfs(walls):
    new_graph = [row[:] for row in graph]

    for x, y in walls:
        new_graph[x][y] = 1

    queue = deque()
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for dx, dy in path:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                queue.append((nx, ny))

    return sum(row.count(0) for row in new_graph)

max_safe = 0
for walls in wall_combs:
    max_safe = max(max_safe, bfs(walls))

print(max_safe)