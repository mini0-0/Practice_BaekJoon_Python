import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    li = list(map(int, input().split()))
    graph.append(li)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상어 시작 위치 찾기
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0

def bfs(x, y, size):
    visited = [[False] * n for _ in range(n)]
    dist = [[0] * n for _ in range(n)]
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    fish_list = []

    while queue:
        cur_x, cur_y = queue.popleft()

        for dir in range(4):
            nx = cur_x + dx[dir]
            ny = cur_y + dy[dir]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = True
                    dist[nx][ny] = dist[cur_x][cur_y] + 1
                    queue.append((nx, ny))

                    if 0 < graph[nx][ny] < size:
                        fish_list.append((dist[nx][ny], nx, ny))

    return sorted(fish_list)

time = 0
shark_size = 2
eat_count = 0

while True:
    fish = bfs(shark_x, shark_y, shark_size)

    if not fish:
        break

    dist, nx, ny = fish[0]
    time += dist
    shark_x, shark_y = nx, ny
    graph[nx][ny] = 0
    eat_count += 1

    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(time)