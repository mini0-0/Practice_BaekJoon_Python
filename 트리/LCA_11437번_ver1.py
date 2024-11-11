import sys

input = sys.stdin.readline
N = int(input())
tree = [[] for _ in range(N+1)]

visited = [False] * (N+1)
parent = [0] * (N+1)
depth = [0] * (N+1)

for _ in range(0, N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def BFS(node):
    q = [node]
    visited[node] = True
    while q :
        now_node = q.pop(0)
        for next in tree[now_node]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                parent[next] = now_node
                depth[next] = depth[now_node] + 1

BFS(1)

def excuteLCA(a, b):
    if depth[a] < depth[b]:
        temp = a
        a = b
        b = temp

    while depth[a] != depth[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


M = int(input())
dic = dict()

for _ in range(M):
    a, b = map(int, input().split())
    if not dic.get((a, b), 0):
        dic[(a, b)] = dic[(b, a)] = excuteLCA(a, b)
    print(dic.get((a, b)))
