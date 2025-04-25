import sys
input = sys.stdin.readline

K, L = map(int, input().split())
dic = {}
for i in range(L):
    dic[input().strip()] = i

answer = sorted(dic.items(), key= lambda x:x[1])

for k in range(min(K, len(answer))):
    print(answer[k][0])