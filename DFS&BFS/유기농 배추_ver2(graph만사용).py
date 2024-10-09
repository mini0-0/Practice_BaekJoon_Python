import sys
sys.setrecursionlimit(10**6)  # 최대 깊이 설정 변경
input = sys.stdin.readline
MAX = 50 + 10  # 최대가 50이지만 여유분으로 +10

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]

def dfs(Y,X) :
    graph[Y][X] = False
    for dirIdx in range(4):
        newY = Y + dirR[dirIdx]
        newX = X + dirC[dirIdx]
        if graph[newY][newX]:
            dfs(newY, newX)

# 1. 입력, 초기화
T = int(input()) # 테스트 케이스의 개수
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]

    # 2. 그래프 정보 입력
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y+1][X+1] = True

    # 3. 방문하지 않은 지점부터 dfs 돌기
    answer = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if graph[i][j] :
                dfs(i, j)
                answer += 1
    print(answer)