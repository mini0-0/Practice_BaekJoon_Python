N = int(input())
m = [0] * N

for i in range(N):
    m[i] = int(input())

for i in range(N-1):
    for j in range(N-1-i):
        if m[j] > m[j+1]:
            temp = m[j]
            m[j] = m[j+1]
            m[j+1] = temp

for i in range(N):
    print(m[i])