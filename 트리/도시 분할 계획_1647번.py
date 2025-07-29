import sys

input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a != b:
        parent[b] = a


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n+1)]

# 유지비 기준으로 정렬
graph.sort(key = lambda x : x[2])
total_cost = 0
last_cost = 0

# union-find로 연결
for i in graph:
    a, b, cost = i
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        total_cost += cost
        last_cost = cost

print(total_cost - last_cost)
