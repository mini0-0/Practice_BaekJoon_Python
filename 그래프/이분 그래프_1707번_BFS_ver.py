import sys
from collections import deque

input = sys.stdin.readline


def BFS(start):
    global IsEven
    queue = deque([start])
    check[start] = 0

    while queue:
        v = queue.popleft()
        for i in A[v]:
            if check[i] == -1:
                check[i] = (check[v] + 1) % 2
                queue.append(i)
            elif check[i] == check[v]:
                IsEven = False
                return


N = int(input())

for _ in range(N):
    V, E = map(int, input().split())
    A = [[] for _ in range(V + 1)]
    check = [-1] * (V + 1)
    IsEven = True

    for _ in range(E):
        Start, End = map(int, input().split())
        A[Start].append(End)
        A[End].append(Start)

    for i in range(1, V + 1):
        if check[i] == -1 and IsEven:
            BFS(i)

    if IsEven:
        print("YES")
    else:
        print("NO")