import sys

N = int(input())
x = []
y = []
answer = 0

for i in range(N):
    inputX, inputY = map(int, input().split())
    x.append(inputX)
    y.append(inputY)

x.append(x[0])
y.append(y[0])

for i in range(N):
    answer += (x[i]*y[i+1]) - (x[i+1] * y[i])

print(round(abs(answer/2), 1))