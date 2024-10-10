N, K = map(int, input().split())
A = list(map(int, input().split()))
sorted_A = sorted(A)

print(sorted_A[K-1])