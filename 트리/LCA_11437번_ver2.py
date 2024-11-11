import sys
import collections
import math

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
tree = [[] for _ in range(N + 1)]
log = int(math.log2(N)) + 1  # log 계산

parent = [[0] * log for _ in range(N + 1)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)

# 트리 정보 입력 받기
for _ in range(N - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def BFS(node):
    q = collections.deque([node])
    visited[node] = True
    while q:
        now_node = q.popleft()
        for next_node in tree[now_node]:
            if not visited[next_node]:
                visited[next_node] = True
                q.append(next_node)
                parent[next_node][0] = now_node  # 2^0 번째 부모
                depth[next_node] = depth[now_node] + 1

BFS(1)

# 모든 노드에 대해 2^i 번째 부모 미리 계산 (sparse table)
for i in range(1, log):
    for j in range(1, N + 1):
        if parent[j][i - 1] != 0:
            parent[j][i] = parent[parent[j][i - 1]][i - 1]

# LCA 함수 (binary lifting 기법)
def excuteLCA(a, b):
    if depth[a] < depth[b]:
        a, b = b, a

    # 깊이를 맞추기
    for i in range(log - 1, -1, -1):
        if depth[a] - depth[b] >= (1 << i):
            a = parent[a][i]

    if a == b:
        return a

    # 공통 조상 찾기
    for i in range(log - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

M = int(input())
result = []
for _ in range(M):
    a, b = map(int, input().split())
    result.append(excuteLCA(a, b))

# 결과 출력
print("\n".join(map(str, result)))
