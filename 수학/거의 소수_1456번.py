import math
min, max = map(int, input().split())
N = 10000001
A = [0] * (N)
count = 0

for i in range(2, len(A)):
    A[i] = i

for i in range(2, int(math.sqrt(len(A))+1)):
    if A[i] == 0:
        continue
    for j in range(i+i, N, i):
        A[j] = 0

for i in range(2, N):
    if A[i] != 0:
        temp = A[i]
        while A[i] <= max/temp:
            if A[i] >= min/temp:
                count += 1
            temp = temp * A[i]
print(count)