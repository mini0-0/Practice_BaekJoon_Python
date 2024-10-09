import math

Min, Max = map(int, input().split())
check = [False] * (Max-Min+1)

for i in range(2, int(math.sqrt(Max))+1):
    pow = i * i
    start_idx = int(Min/pow)
    if Min % pow != 0:
        start_idx += 1
    for j in range(start_idx, int(Max/pow)+1):
        check[int((j*pow) - Min)] = True

count = 0

for i in range(0, Max-Min+1):
    if not check[i]:
        count += 1

print(count)