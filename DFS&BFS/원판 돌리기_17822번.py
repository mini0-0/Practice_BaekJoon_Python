import sys
from collections import deque

input = sys.stdin.readline
n, m, t = map(int, input().split())
board = [deque(map(int, input().split())) for _ in range(n)]
commands = [tuple(map(int, input().split())) for _ in range(t)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, val, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    to_remove = [(x, y)]
    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = (cy + dy[i]) % m
            if 0 <= nx < n and not visited[nx][ny] and board[nx][ny] == val:
                visited[nx][ny] = True
                q.append((nx, ny))
                to_remove.append((nx, ny))
    return to_remove if len(to_remove) > 1 else []

for x, d, k in commands:
    # 1. 회전
    for i in range(n):
        if (i + 1) % x == 0:
            board[i].rotate(k if d == 0 else -k)

    # 2. 인접 숫자 제거
    visited = [[False] * m for _ in range(n)]
    remove_set = set()

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and not visited[i][j]:
                remove_set.update(bfs(i, j, board[i][j], visited))

    if remove_set:
        for x, y in remove_set:
            board[x][y] = 0
    else:
        # 3. 평균 조정
        total, count = 0, 0
        for i in range(n):
            for j in range(m):
                if board[i][j] != 0:
                    total += board[i][j]
                    count += 1

        if count == 0:
            continue

        avg = total / count

        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    continue
                if board[i][j] > avg:
                    board[i][j] -= 1
                elif board[i][j] < avg:
                    board[i][j] += 1

# 4. 최종 결과
print(sum(sum(row) for row in board))
