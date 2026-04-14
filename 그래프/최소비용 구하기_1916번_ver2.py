import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

dist = [sys.maxsize] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start_idx, end_idx = map(int, input().split())

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        current_dist, now_node = heapq.heappop(q)

        if dist[now_node] < current_dist:
            continue

        for next_node, weight in graph[now_node]:
            new_dist = dist[now_node] + weight

            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))

    return dist[end]


print(dijkstra(start_idx, end_idx))