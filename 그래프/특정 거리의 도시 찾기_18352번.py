import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
A = [[] for _ in range(N+1)]
answer = []
visited = [-1] * (N+1)


def BFS(v):
    q = deque()
    q.append(v)
    visited[v] += 1
    while q:
        now = q.popleft()
        for i in A[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                q.append(i)

for i in range(M):
    S, E = map(int, input().split())
    A[S].append(E)

BFS(X)

for i in range(N+1):
    if visited[i] == K:
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)