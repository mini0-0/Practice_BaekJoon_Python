import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N)]
visited = [False] * (N)
answer = 0
p = list(map(int, input().split()))
del_num = int(input())

for i in range(N):
    if p[i] != -1:
        tree[i].append(p[i])
        tree[p[i]].append(i)
    else:
        root = i

def DFS(num):
    global answer
    visited[num] = True
    cNode = 0
    for i in tree[num]:
        if not visited[i] and i != del_num:
            cNode += 1
            DFS(i)
    if cNode == 0:
        answer += 1

if del_num == root:
    print(0)
else:
    DFS(root)
    print(answer)
