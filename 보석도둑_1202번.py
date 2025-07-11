import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
jewels = []
bags = []
for _ in range(n):
    m, v = map(int, input().split())
    jewels.append((m,v))

for _ in range(k):
    cnt = int(input())
    bags.append(cnt)

jewels.sort()
bags.sort()

heap = []
i = 0
answer = 0

for bag in bags:
    while i < n and jewels[i][0] <= bag:
        heapq.heappush(heap, -jewels[i][1])
        i += 1

    if heap:
        answer += -heapq.heappop(heap)

print(answer)