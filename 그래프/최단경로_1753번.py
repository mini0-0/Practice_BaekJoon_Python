import sys
from queue import PriorityQueue
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
A = [[] for i in range(V+1)]
dist = [sys.maxsize] * (V+1)
visited = [False] * (V+1)
q = PriorityQueue()

for i in range(E):
    u, v, w = map(int, input().split())
    A[u].append((v, w))

q.put((0, K))
dist[K] = 0
while q.qsize() > 0:
    now = q.get()
    now_v = now[1]
    if visited[now_v]:
        continue
    visited[now_v] = True
    for tmp in A[now_v]:
        next = tmp[0]
        value = tmp[1]
        if dist[next] > dist[now_v] + value:
            dist[next] = dist[now_v] + value
            q.put((dist[next], next))

for i in range(1, V+1):
    if visited[i]:
        print(dist[i])
    else:
        print("INF")