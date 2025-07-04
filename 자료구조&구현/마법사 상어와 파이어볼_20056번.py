import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
fireballs = []

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r-1, c-1, m, s, d))

# 8방향
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

def move(fireballs):
    grid = [[[] for _ in range(N)] for _ in range(N)]
    for r, c, m, s, d in fireballs:
        nr = (r + dr[d] * s) % N
        nc = (c + dc[d] * s) % N
        grid[nr][nc].append((m, s, d))
    return grid

def merge(grid):
    new_fireballs = []
    for i in range(N):
        for j in range(N):
            if not grid[i][j]:
                continue
            if len(grid[i][j]) == 1:
                m, s, d = grid[i][j][0]
                new_fireballs.append((i, j, m, s, d))
            else:
                count = len(grid[i][j])
                total_m = sum(m for m, _, _ in grid[i][j])
                total_s = sum(s for _, s, _ in grid[i][j])
                new_m = total_m // 5
                if new_m == 0:
                    continue

                new_s = total_s // count
                first_parity = grid[i][j][0][2] % 2
                same_parity = all(d % 2 == first_parity for _, _, d in grid[i][j])
                directions = [0,2,4,6] if same_parity else [1,3,5,7]
                for d in directions:
                    new_fireballs.append((i, j, new_m, new_s, d))
    return new_fireballs

for _ in range(K):
    grid = move(fireballs)
    fireballs = merge(grid)

print(sum(m for _, _, m, _, _ in fireballs))
