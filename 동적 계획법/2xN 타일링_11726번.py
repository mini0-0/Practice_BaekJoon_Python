import sys

input = sys.stdin.readline
N = int(input())
D = [0] * 10001
D[1] = 1
D[2] = 2
mod = 10007

for i in range(3, N+1):
    D[i] = (D[i-1] + D[i-2]) % mod

print(D[N])