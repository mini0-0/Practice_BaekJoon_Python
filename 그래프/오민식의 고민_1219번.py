import sys
input = sys.stdin.readline

N, sCity, eCity, M = map(int, input().split())
edges = []
dist = [-sys.maxsize] * (N+1)

for _ in range(M):
    start, end, price = map(int, input().split())
    edges.append((start, end, price))

cityMoney = list(map(int, input().split()))

dist[sCity] = cityMoney[sCity]

for i in range(N+101):
    for start, end, price in edges:
        if dist[start] == (-sys.maxsize):
            continue
        if dist[start] == (sys.maxsize):
            dist[end] = sys.maxsize
        elif dist[end] < dist[start] + cityMoney[end] - price:
            dist[end] = dist[start] + cityMoney[end] - price
            if i >= N-1:
                dist[end] = sys.maxsize

if dist[eCity] == (-sys.maxsize):
    print("gg")
elif dist[eCity] == sys.maxsize:
    print("Gee")
else:
    print(dist[eCity])