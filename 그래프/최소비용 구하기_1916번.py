# import sys
# from queue import PriorityQueue
#
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# dist = [sys.maxsize] * (N+1)
# A = [[] for _ in range(N+1)]
# visited = [False] * (N+1)
#
# for _ in range(M):
#     start, end, weight = map(int, input().split())
#     A[start].append((end, weight))
#
# start_idx, end_idx = map(int, input().split())
#
# def dijkstra(start, end):
#     q = PriorityQueue()
#     q.put((0, start))
#     dist[start] = 0
#
#     while q.qsize() > 0:
#         now = q.get()
#         now_v = now[1]
#
#         if visited[now_v]:
#             continue
#         visited[now_v] = True
#
#         for tmp in A[now_v]:
#             next = tmp[0]
#             value = tmp[1]
#             if dist[next] > dist[now_v] + value:
#                 dist[next] = dist[now_v] + value
#                 q.put((dist[next], next))
#     return dist[end]
#
# print(dijkstra(start_idx, end_idx))

import sys
from queue import PriorityQueue
input = sys.stdin.readline

N = int(input())
M = int(input())
dist = [sys.maxsize] * (N+1)
A = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    start, end, weight = map(int, input().split())
    A[start].append((end, weight))

start_idx, end_idx = map(int, input().split())

def dijkstra(start, end):
    q = PriorityQueue()
    q.put((0, start))
    dist[start] = 0

    while q.qsize() > 0:
        now = q.get()
        now_v = now[1]

        if not visited[now_v]:
            visited[now_v] = True
            for tmp in A[now_v]:
                next = tmp[0]
                value = tmp[1]
                if dist[next] > dist[now_v] + value:
                    dist[next] = dist[now_v] + value
                    q.put((dist[next], next))

    return dist[end]

print(dijkstra(start_idx, end_idx))