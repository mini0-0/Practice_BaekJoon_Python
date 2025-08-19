n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
count0 = 0
count1 = 0
count_m1 = 0


def div(x, y, n):
    global count0, count1, count_m1
    check = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                check = -2
                break

    if check == -2:
        n = n // 3
        div(x, y, n)
        div(x, y + n, n)
        div(x, y + 2 * n, n)
        div(x + n, y, n)
        div(x + n, y + n, n)
        div(x + n, y + 2 * n, n)
        div(x + 2 * n, y, n)
        div(x + 2 * n, y + n, n)
        div(x + 2 * n, y + 2 * n, n)

    elif check == 1:
        count1 += 1

    elif check == 0:
        count0 += 1
    else:
        count_m1 += 1


div(0, 0, n)
print(count_m1)
print(count0)
print(count1)
