import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
command = [list(map(int, input().split())) for _ in range(m)]

path = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
diag_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


# 초기 구름 설정
clouds = deque([(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)])

for d, s in command:
    d -= 1
    visited = [[False] * n for _ in range(n)]
    new_clouds = deque()

    # 구름 이동
    while clouds:
        x, y = clouds.popleft()
        dx, dy = path[d]
        nx = (x + dx * s) % n
        ny = (y + dy * s) % n

        # 물 증가
        arr[nx][ny] += 1
        visited[nx][ny] = True
        new_clouds.append((nx, ny))

    # 물 복사 마법
    for x, y in new_clouds:
        count = 0
        for dx, dy in diag_dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > 0:
                count += 1

        arr[x][y] += count


    # 구름 생성
    clouds = deque()
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and arr[i][j] >= 2:
                arr[i][j] -= 2
                clouds.append((i, j))

print(sum(sum(row) for row in arr))