import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

for _ in range(K):
    x, y = map(int, input().split())
    graph[x][y] = 1

L = int(input())
directions = dict()
for _ in range(L):
    t, d = input().split()
    directions[int(t)] = d

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

snake = deque()
snake.append((1, 1))
time = 0
x, y = 1, 1

while True:
    time += 1
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not (1 <= nx <= N and 1 <= ny <= N):
        break
    if (nx, ny) in snake:
        break

    snake.appendleft((nx, ny))

    if graph[nx][ny] == 1:
        graph[nx][ny] = 0
    else:
        snake.pop()

    if time in directions:
        if directions[time] == 'D':
            dir = (dir + 1) % 4
        else:
            dir = (dir - 1) % 4

    x, y = nx, ny

print(time)