import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
    n = int(input())
    arrs = list(map(int, input().split()))
    arrs.insert(0, 0)

    visited = [False] * (n + 1)
    finished = [False] * (n + 1)
    count = 0

    def dfs(current):
        global count
        visited[current] = True
        next_node = arrs[current]

        if not visited[next_node]:
            dfs(next_node)

        elif not finished[next_node]:
            node = next_node
            while node != current:
                count += 1
                node = arrs[node]

            count += 1

        finished[current] = True


    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i)

    print(n - count)