import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
A = [[] for _ in range(N + 1)]
answer = [0] * (N + 1)

def BFS(v):
    visited = [False] * (N + 1)
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                answer[i] += 1
                q.append(i)



for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

for i in range(1, N+1):
    BFS(i)

MAX = max(answer)
for i in range(1, N+1):
    if MAX == answer[i]:
        print(i, end=" ")