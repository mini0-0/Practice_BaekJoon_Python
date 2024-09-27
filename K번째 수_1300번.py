n = int(input())
k = int(input())

start = 1
end = k
ans = 0

while start <= end:
    mid = int((start+end)/2)
    cnt = 0
    for i in range(1, n+1):
        cnt += min(int(mid/i), n)
    if cnt < k:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)