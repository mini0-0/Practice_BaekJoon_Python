import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y,x):
    global visited, graph
    visited[y][x]=True

    if graph[y][x] == '-' and graph[y][x+1] == '-':
        dfs(y, x+1)
    elif graph[y][x] == '|' and graph[y+1][x] == '|':
        dfs(y+1, x)

N,M = map(int, input().split())
MAX = 50+10
graph = [[''] * MAX for _ in range(MAX) ]
visited = [[False] * MAX for _ in range(MAX) ]

for i in range(1,N+1):
    line = input()
    for j in range(1, M+1):
        graph[i][j] = line[j-1]

answer = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if not visited[i][j]:
            dfs(i,j)
            answer += 1

print(answer)
