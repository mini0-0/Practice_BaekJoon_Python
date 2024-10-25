import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
dist = [[sys.maxsize] * K for _ in range(N+1)]
A = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    A[a].append((b, c))

q = [(0, 1)]
dist[1][0] = 0
while q:
    cost, node = heapq.heappop(q)
    for nNode, nCost in A[node]:
        total_cost = cost + nCost
        if dist[nNode][K - 1] > total_cost:
            dist[nNode][K - 1] = total_cost
            dist[nNode].sort()
            heapq.heappush(q,[total_cost, nNode])

for i in range(1, N+1):
    if dist[i][K-1] == sys.maxsize:
        print(-1)
    else:
        print(dist[i][K-1])