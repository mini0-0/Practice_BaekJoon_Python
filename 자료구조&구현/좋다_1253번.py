import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort()

answer = 0

for k in range(N):
    find = A[k]
    start = 0
    end = N - 1
    while start < end:
        if A[start] + A[end] == find :
            if start != k and end != k:
                answer += 1
                break
            elif start == k:
                start += 1
            else:
                end -= 1

        elif A[start] + A[end] < find:
            start += 1
        else:
            end -= 1

print(answer)