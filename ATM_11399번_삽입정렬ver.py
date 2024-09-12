N = int(input())
P = list(map(int, input().split()))
S = [0]*N

for i in range(1, N):
    insert_point = i
    insert_value = P[i]

    for j in range(i-1, -1, -1):
        if P[j] < P[i]:
            insert_point = j+1
            break

        if j==0:
            insert_point=0

    for j in range(i, insert_point, -1):
        P[j] = P[j-1]
    P[insert_point] = insert_value

S[0] = P[0]

for i in range(1, N):
    S[i] = S[i-1] + P[i]

sum = 0

for i in range(0, N):
    sum += S[i]
print(sum)