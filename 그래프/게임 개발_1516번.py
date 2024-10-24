from collections import deque

N = int(input())
A = [[] for i in range(N+1)]
indegree = [0] * (N+1)
build = [0] * (N+1)

for i in range(1,N+1):
    li = list(map(int, input().split()))
    build[i] = li[0] # 건물을 짓는데 걸리는 시간
    index = 1
    while True:
        preTmp = li[index]
        index += 1
        if preTmp == -1:
            break
        A[preTmp].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

result = [0] * (N+1)

while q:
    now = q.popleft()
    for next in A[now]:
        indegree[next] -= 1
        result[next] = max(result[next], result[now] + build[now])
        if indegree[next] == 0:
            q.append(next)

for i in range(1, N+1):
    print(result[i]+build[i])