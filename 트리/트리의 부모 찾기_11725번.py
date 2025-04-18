import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
tree = [[]for _ in range(N+1)]
visited = [False] * (N+1)
answer = [0] * (N+1)

for i in range(1, N):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def DFS(num):
    visited[num] = True
    for i in tree[num]:
        if not visited[i]:
            answer[i] = num
            DFS(i)

DFS(1)

for i in range(2, N+1):
    print(answer[i])