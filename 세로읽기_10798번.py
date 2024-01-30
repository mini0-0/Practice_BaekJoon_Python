import sys
input = sys.stdin.readline

dic = [input().strip() for _ in range(5)]

for x in range(15):
    for y in range(5):
        if x < len(dic[y]):
            print(dic[y][x],end='')