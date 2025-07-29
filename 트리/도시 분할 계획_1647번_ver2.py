import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a == b:
        return

    if rank[a] < rank[b]:
        parent[a] = b
    else:
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)
graph.sort(key=lambda x: x[2])

total_cost = 0
last_cost = 0

for a, b, cost in graph:
    if find(parent, a) != find(parent, b):
        union(parent, rank, a, b)
        total_cost += cost
        last_cost = cost

print(total_cost - last_cost)