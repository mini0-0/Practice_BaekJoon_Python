from collections import deque

N = int(input())
M = int(input())
A = [[] for i in range(N+1)]
reverse_A = [[] for i in range(N+1)]
indegree = [0] * (N+1)
result = [0] *(N+1)

for i in range(M):
    S, E, V = map(int, input().split())
    A[S].append((E,V))
    reverse_A[E].append((S,V))
    indegree[E] += 1

startDosi, endDosi = map(int, input().split())

q = deque()
q.append(startDosi)

while q:
    now = q.popleft()
    for next in A[now]:
        indegree[next[0]] -= 1
        result[next[0]] = max(result[next[0]], result[now] + next[1])
        if indegree[next[0]] == 0:
            q.append(next[0])

cnt = 0
visited = [False] * (N+1)
q.clear()
q.append(endDosi)
visited[endDosi] = True

while q:
    now = q.popleft()
    for next in reverse_A[now]:
        if result[next[0]] + next[1] == result[now]:
            cnt += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                q.append(next[0])
print(result[endDosi])
print(cnt)