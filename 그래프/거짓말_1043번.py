import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())
trueP = list(map(int, input().split()))
T = trueP[0] # 진실을 알고 있는 사람 수
del trueP[0] # 진실을 알고 있는 사람의 번호만 남기기
party = [[] for _ in range(M)]
parent = [0] * (N + 1)
count = 0

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b :
        parent[b] = a


for i in range(M): # party값 저장
    party[i] = list(map(int, input().split()))
    del party[i][0]

for i in range(N + 1): # parent 자기 자신으로 초기화
    parent[i] = i

for i in range(M): # 각 파티에 참여한 사람들을 1개의 그룹으로 만들기
    firstPeople = party[i][0]
    for j in range(1, len(party[i])):
        union(firstPeople, party[i][j])

for i in range(M):
    IsPossible = True
    firstPeople = party[i][0]
    for j in range(len(trueP)):
        # 각 파티의 대표 노드와 TrueP가 대표 노트가 같으면 과장 할 수 X
        if find(firstPeople) == find(trueP[j]):
            IsPossible = False
            break

    if IsPossible:
        count += 1

print(count)