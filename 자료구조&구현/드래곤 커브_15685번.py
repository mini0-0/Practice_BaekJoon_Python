import sys

input = sys.stdin.readline
n = int(input())

path = [(1, 0), (0, -1), (-1, 0), (0, 1)]
board = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())

    board[x][y] = 1
    curve = [d]

    for _ in range(g):
        for i in range(len(curve)-1, -1, -1):
            curve.append((curve[i]+1) % 4)

    cx, cy = x, y
    for c in curve:
        dx, dy = path[c]
        cx += dx
        cy += dy

        if 0 <= cx <= 100 and 0 <= cy <= 100:
            board[cx][cy] = 1


answer = 0

for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            answer += 1

print(answer)