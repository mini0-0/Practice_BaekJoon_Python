import sys

input = sys.stdin.readline

r, c, n = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
path = [(-1, 0), (1, 0),(0, -1),(0, 1)]

def bomb(board):
    to_bomb = set()
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                to_bomb.add((i, j))
                for dx, dy in path:
                    nx = i + dx
                    ny = j + dy
                    if 0 <= nx < r and 0 <= ny < c:
                        to_bomb.add((nx, ny))

    new_board = [['O'] * c for _ in range(r)]
    for x, y in to_bomb:
        new_board[x][y] = '.'

    return new_board

if n == 1:
    for i in range(r):
        print(''.join(board[i]))

elif n % 2 == 0:
    for i in range(r):
        print('O' * c)

elif n % 4 == 3:
    board = bomb(board)
    for row in board:
        print(''.join(row))

elif n % 4 == 1 and n > 1:
    board = bomb(bomb(board))
    for row in board:
        print(''.join(row))