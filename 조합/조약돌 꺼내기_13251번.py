import sys

input = sys.stdin.readline

M = int(input())
D = list(map(int, input().split()))
K = int(input())
T = 0
probability = [0] * 51
count = 0

for i in range(0, M):
    T += D[i]

for i in range(0, M):
    if D[i] >= K:
        probability[i] = 1
        for k in range(0, K):
            probability[i] = probability[i] * (D[i]-k) / (T-k)
        count += probability[i]

print(count)