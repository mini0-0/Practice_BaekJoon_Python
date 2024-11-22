import sys

input = sys.stdin.readline
D = [[[sys.maxsize for k in range(5)]for j in range(5)]for i in range(100001)]

mp = [[0, 2, 2, 2, 2],
      [2, 1, 3, 4, 3],
      [2, 3, 1, 3, 4],
      [2, 4, 3, 1, 3],
      [2, 3, 4, 3, 1]]

s = 1
D[0][0][0] = 0

li = list(map(int, input().split()))
index = 0

while li[index] != 0:
    n = li[index]
    for i in range(5):
        if n == i:
            continue
        for j in range(5):
            D[s][i][n] = min(D[s-1][i][j]+mp[j][n], D[s][i][n])

        for j in range(5):
            if n == j:
                continue
            for i in range(5):
                D[s][n][j] = min(D[s - 1][i][j] + mp[i][n], D[s][n][j])
    s += 1
    index += 1

s -= 1
result = sys.maxsize

for i in range(5):
    for j in range(5):
        result = min(result, D[s][i][j])

print(result)