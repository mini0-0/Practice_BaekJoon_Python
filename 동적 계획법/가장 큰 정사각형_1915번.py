import sys

input = sys.stdin.readline
n, m = map(int, input().split())
D = [[0 for j in range(1001)] for i in range(1001)]
MAX = 0

for i in range(0, n):
    num = list(input())
    for j in range(0, m):
        D[i][j] = int(num[j])
        if D[i][j] == 1 and j > 0 and i > 0:
            D[i][j] = min(D[i-1][j-1], D[i][j-1], D[i-1][j]) + D[i][j]
        if MAX < D[i][j]:
            MAX = D[i][j]
print(MAX*MAX)