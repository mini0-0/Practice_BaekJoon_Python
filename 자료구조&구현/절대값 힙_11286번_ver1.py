from queue import PriorityQueue
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
Q = PriorityQueue()

for i in range(N):
    num = int(input())
    if num == 0:
        if Q.empty():
            print('0\n')
        else:
            temp = Q.get()
            print(str((temp[1]))+'\n')
    else:
        Q.put((abs(num), num))