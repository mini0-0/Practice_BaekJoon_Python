from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    data = list(map(int, input().split()))
    idx = 0
    S = data[idx]
    idx += 1

    while True:
        E = data[idx]
        if E == -1:
            break

        V = data[idx+1]
        A[S].append((E, V))
        idx += 2

distance = [0] * (N + 1)
visited = [False] * (N + 1)

def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        now = q.popleft()
        for i in A[now]:
            if not visited[i[0]]:
                visited[i[0]] = True
                q.append(i[0])
                distance[i[0]] = distance[now] + i[1]

BFS(1)
MAX = 1

for i in range(2, N+1):
    if distance[MAX] < distance[i]:
        MAX = i

distance = [0] * (N + 1)
visited = [False] * (N + 1)
BFS(MAX)
distance.sort()
print(distance[N])