import sys
from collections import deque
input = sys.stdin.readline

N, L = map(int, input().split())
A = list(map(int, input().split()))
answer = deque()

for i in range(N):
    while answer and answer[-1][0] > A[i]:
        answer.pop()
    answer.append((A[i],i))
    if answer[0][1] <= i-L:
        answer.popleft()
    print(answer[0][0], end=" ")