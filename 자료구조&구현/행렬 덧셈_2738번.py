import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = []
B = []
for _ in range(N):
    row = list(map(int,input().split()))
    A.append(row)

for _ in range(N):
    row = list(map(int,input().split()))
    B.append(row)

for y in range(N):
    for x in range(M):
        print(A[y][x]+B[y][x],end =' ')
    print()
