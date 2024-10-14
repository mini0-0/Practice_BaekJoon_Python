from collections import deque

sender = [0, 0, 1, 1, 2, 2]
receiver = [1, 2, 0, 2, 0, 1]
now = list(map(int, input().split()))
visited = [[False for j in range(201)] for i in range(201)]
answer = [False] * 201

def BFS():
    q = deque()
    q.append((0, 0))
    visited[0][0] = True
    answer[now[2]] = True
    while q:
        now_node= q.popleft()
        A = now_node[0]
        B = now_node[1]
        C = now[2] - A - B
        for k in range(6):
            next = [A, B, C]
            next[receiver[k]] += next[sender[k]]
            next[sender[k]] = 0
            if next[receiver[k]] > now [receiver[k]]:
                next[sender[k]] = next[receiver[k]] - now[receiver[k]]
                next[receiver[k]] = now[receiver[k]]
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                q.append((next[0], next[1]))
                if next[0] == 0:
                    answer[next[2]] = True

BFS()

for i in range(len(answer)):
    if answer[i]:
        print(i, end=" ")