N = int(input())
arr = []

for i in range(N):
    a,b = map(int,input().split())
    arr.append((a,b))

arr.sort(key=lambda x:(x[1],x[0]))
room = 1
check = arr[0][1]

for j in range(1,N):
    if arr[j][0] >= check:
        check = arr[j][1]
        room +=1
print(room)