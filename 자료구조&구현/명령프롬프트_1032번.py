import sys
input = sys.stdin.readline

N = int(input())
n_list = [input().strip() for i in range(N)]

answer = ''
for i in range(len(n_list[0])):
    char = n_list[0][i]
    for j in range(N):
        if n_list[j][i] !=char:
            char ='?'
            break
    answer += char

print(answer)