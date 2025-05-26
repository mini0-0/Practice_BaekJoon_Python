import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * (N+1)
visited = [False] * (N+1)
answer = set()
def DFS(start, current, path):
    visited[current] = True
    path.append(current)
    next_node = arr[current]

    if not visited[next_node]:
        DFS(start, next_node, path)
    elif next_node == start:
        answer.update(path)

    visited[current] = False

for i in range(1, N+1):
    arr[i] = int(input())

for j in range(1, N+1):
    if j not in answer:
        DFS(j,j,[])

print(len(answer))
for i in sorted(answer):
    print(i)
