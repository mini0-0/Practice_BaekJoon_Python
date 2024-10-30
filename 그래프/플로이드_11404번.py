import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
dist = [[sys.maxsize for j in range(N+1)] for i in range(N+1)]

for i in range(N+1):
    dist[i][i] = 0

for _ in range(M):
    start, end, price = map(int, input().split())
    if dist[start][end] > price:
        dist[start][end] = price

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, N+1):
    for j in range(1, N+1):
        if dist[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(dist[i][j], end=" ")
    print()