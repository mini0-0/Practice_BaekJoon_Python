import math

num = int(input())
N = 10000001
A = [0]*(N+1)

for i in range(2, N+1):
    A[i] = i

for i in range(2, int(math.sqrt(N))+1):
    if A[i] == 0:
        continue
    for j in range(i+i, N, i):
        A[j] = 0

def isPalindrome(target):
    temp = list(str(target))
    start = 0
    end = len(temp) - 1
    while start < end:
        if temp[start] != temp[end]:
            return False
        start += 1
        end -= 1
    return True

k = num
while True:
    if A[k] != 0:
        result = A[k]
        if(isPalindrome(result)):
            print(result)
            break
    k += 1