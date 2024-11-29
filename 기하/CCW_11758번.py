import sys

input = sys.stdin.readline

A = []
for i in range(3):
    x, y = map(int, input().split())
    A.append((x,y))

result = (A[0][0] * A[1][1] + A[1][0] * A[2][1] + A[2][0] * A[0][1]) - (A[1][0] * A[0][1] + A[2][0] * A[1][1] + A[0][0] * A[2][1])
if result < 0:
    print(-1)
elif result == 0:
    print(0)
else:
    print(1)