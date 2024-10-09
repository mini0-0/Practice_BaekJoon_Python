import sys
N = int(input())
A = list(map(int, input().split()))
s = [0]*N
stack = []

for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        s[stack.pop()] = A[i]
    stack.append(i)
while stack:
    s[stack.pop()] = -1

for i in range(N):
    sys.stdout.write(str(s[i]) + " ")