from collections import deque
N, M = map(int, input().split())
A = [[]for i in range(N+1)]
indegree = [0] * (N+1)

for i in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    indegree[e] += 1

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    print(now, end=" ")
    for j in A[now]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)