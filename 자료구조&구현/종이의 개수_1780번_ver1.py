import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

cnt_zero = 0
cnt_one = 0
cnt_m_one = 0

def divide(x, y, size):
    global cnt_zero, cnt_one, cnt_m_one
    first = arr[x][y]
    same = True

    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != first:
                same = False
                break
        if not same:
            break

    if same:
        if first == -1:
            cnt_m_one += 1
        elif first == 0:
            cnt_zero += 1
        else:
            cnt_one += 1
        return
    else:
        new_size = size // 3
        for i in range(3):
            for j in range(3):
                divide(x + i * new_size, y + j * new_size, new_size)

divide(0, 0, n)

print(cnt_m_one)
print(cnt_zero)
print(cnt_one)