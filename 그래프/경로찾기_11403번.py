import sys
input = sys.stdin.readline

N = int(input())
dist = [[0 for j in range(N)]for i in range(N)]

for i in range(N):
    dist[i] = list(map(int, input().split()))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][k] == 1 and dist[k][j] == 1:
                dist[i][j] = 1

for i in range(N):
    for j in range(N):
        print(dist[i][j], end=" ")
    print()