import sys
input = sys.stdin.readline
edges = []
N, M = map(int, input().split())
dist = [sys.maxsize] * (N+1)

# 에지 데이터 저장
for i in range(M):
    start, end, time = map(int, input().split())
    edges.append((start, end, time))

#베만 포드 수행
dist[1] = 0

for _ in range(N+1):
    for start, end, time in edges:
        if dist[start] != sys.maxsize and dist[end] > dist[start] + time:
            dist[end] = dist[start] + time

# 음수 사이클 확인
mCycle = False

for start, end, time in edges:
    if dist[start] != sys.maxsize and dist[end] > dist[start] + time:
        mCycle = True

if not mCycle:
    for i in range(2, N+1):
        if dist[i] != sys.maxsize:
            print(dist[i])
        else:
            print(-1)
else:
    print(-1)