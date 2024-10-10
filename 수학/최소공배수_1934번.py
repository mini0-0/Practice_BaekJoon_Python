n = int(input())
def gcd(A,B):
    if B==0:
        return A
    else:
        return gcd(B, A%B)

for i in range(n):
    A, B = map(int, input().split())
    result = A * B / gcd(A, B)
    print(int(result))