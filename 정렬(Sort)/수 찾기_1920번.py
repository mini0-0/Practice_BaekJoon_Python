N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
target = list(map(int, input().split()))

for i in range(M):
    f = False
    t = target[i]

    start = 0
    end = len(A) - 1

    while start <= end:
        mid = int((start+end) / 2)
        midv = A[mid]
        if midv > t:
            end = mid - 1
        elif midv < t:
            start = mid + 1
        else:
            f = True
            break

    if f:
        print(1)
    else:
        print(0)