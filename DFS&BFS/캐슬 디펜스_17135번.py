import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
archers = list(combinations(range(m), 3))
path = [(0, -1), (-1, 0), (0, 1)]

def bfs(row, col, temp_map):
    visited = [[False] * m for _ in range(n)]
    queue = deque()
    queue.append((row, col, 1))

    while queue:
        x, y, dist = queue.popleft()
        if dist > d:
            break
        if 0 <= x < n and 0 <= y < m and not visited[x][y]:
            visited[x][y] = True
            if temp_map[x][y] == 1:
                return (x, y)
            for dx, dy in path:
                nx = x + dx
                ny = y + dy
                queue.append((nx, ny, dist + 1))
    return None


def kill(archers):
    temp_map = [row[:] for row in graph]
    total_kill = 0

    for _ in range(n):
        targets = set()

        for col in archers:
            target = bfs(n -1 , col, temp_map)
            if target:
                targets.add(target)

        for x, y in targets:
            if temp_map[x][y] == 1:
                temp_map[x][y] = 0
                total_kill += 1


        temp_map.pop()
        temp_map.insert(0, [0] * m)

    return total_kill


answer = 0

for archer in archers:
    answer = max(answer, kill(archer))

print(answer)
