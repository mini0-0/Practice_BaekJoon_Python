import sys

input = sys.stdin.readline
mod = 1000000007
N, L, R = map(int, input().split())

D = [[[0 for k in range(101)]for j in range(101)]for i in range(101)]
D[1][1][1] = 1

for n in range(2, N+1):
    for l in range(1, L+1):
        for r in range(1, R+1):
            D[n][l][r] = ((D[n-1][l-1][r] + D[n-1][l][r-1]) + D[n-1][l][r] * (n-2)) % mod

print(D[N][L][R])