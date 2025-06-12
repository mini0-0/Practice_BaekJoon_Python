import sys
import heapq
input = sys.stdin.readline

time = []
heap = []
N = int(input())
for _ in range(N):
    time.append(list(map(int, input().split())))

time.sort(key = lambda x : (x[0], x[1]))

for start, end in time:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))