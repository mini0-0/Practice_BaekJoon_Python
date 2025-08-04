import sys
import copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split()))for _ in range(n)]

path = [(-1, 0), (1, 0), (0, 1),(0, -1)]
comb = []

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            comb.append((i, j))

comb = list(combinations(comb, 3))

def bfs(graph, comb):
    new_graph = copy.deepcopy(graph)

    for x, y in comb:
        new_graph[x][y] = 1

    queue = deque()
    for i in range(n):
        for j in range(m):
            if new_graph[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for dx, dy in path:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and new_graph[nx][ny] == 0:
                new_graph[nx][ny] = 2
                queue.append((nx, ny))

    return sum(row.count(0) for row in new_graph)

max_safe = 0
for c in comb:
    safe = bfs(graph, c)
    max_safe = max(max_safe, safe)
print(max_safe)