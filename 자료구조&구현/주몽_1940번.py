import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
A = list(map(int, input().split()))
A.sort()

start = 0
end = N-1
answer = 0

while start < end:
    if A[start] + A[end] < M:
        start += 1
    elif A[start] + A[end] > M:
        end -= 1

    else:
        start += 1
        end -= 1
        answer +=1

print(answer)
