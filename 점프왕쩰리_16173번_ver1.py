import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [0, 1]
dirX = [1, 0]
def dfs(y,x):
    global graph, visited, N
    visited[y][x] = True

    if y == N and x == N:
        return

    for dirIdx in range(2):
        newY = y + dirY[dirIdx] * graph[y][x]
        newX = x + dirX[dirIdx] * graph[y][x]
        if not visited[newY][newX]:
            dfs(newY, newX)

N = int(input())
MAX = 3 + 100+ 10

graph = [[0] * MAX for _ in range(MAX)]
visited = [[False] * MAX for _ in range(MAX)]

for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in range(1, N+1):
        graph[i][j] = line[j - 1]

dfs(1,1)

print("HaruHaru" if visited[N][N] else "Hing")