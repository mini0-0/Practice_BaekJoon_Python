import sys
input = sys.stdin.readline

dic = []
answer = [[0,0]]
Max = 0

for _ in range(9):
    line = list(map(int,input().split()))
    dic.append(line)

for y in range(9):
    for x in range(9):
        if dic[y][x] >= Max:
            Max = dic[y][x]
            answer.append([y+1,x+1])
            answer.pop(0)

print(Max)
print(answer[0][0], answer[0][1])