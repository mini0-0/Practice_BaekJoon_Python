import sys
import heapq

input = sys.stdin.readline

x = int(input())
heap = []
for _ in range(x):
    num = int(input())
    if num == 0:
        try:
            print(heapq.heappop(heap)[1])

        except:

            print(0)

    else:
        heapq.heappush(heap, (abs(num), num))
