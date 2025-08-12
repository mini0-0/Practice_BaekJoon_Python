import sys

input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))

        elif graph[i][j] == 2:
            chicken.append((i, j))

house_perms = combinations(chicken, m)

answer = float("inf")

for house_perm in house_perms:
    city_distance = 0

    for h in house:
        min_dist = float("inf")
        for hp in house_perm:
            dist = abs(h[0] - hp[0]) + abs(h[1] - hp[1])
            min_dist = min(min_dist, dist)

        city_distance += min_dist
    answer = min(answer, city_distance)

print(answer)
