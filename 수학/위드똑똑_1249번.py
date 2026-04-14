import sys
from math import comb

input = sys.stdin.readline
MOD = 1234567891

def sum_geo(r, m):
    if m <= 0: return 0
    if m == 1: return r % MOD

    if m % 2 == 0:
        half = sum_geo(r, m // 2)
        return (half * (1 + pow(r, m // 2, MOD))) % MOD

    return (r + r * sum_geo(r, m - 1)) % MOD


n, k = map(int, input().split())

m_limit = (n + 1) // 2
f = [0] * (k + 1)
ans = 0

for i in range(1, k + 1):
    total = (2 * sum_geo(i, m_limit)) % MOD

    if n % 2 == 1:
        total = (total - pow(i, m_limit, MOD)) % MOD

    res = total
    for j in range(1, i):
        res = (res - comb(i, j) * f[j]) % MOD

    f[i] = res

    ans = (ans + comb(26, i) * f[i]) % MOD

print(ans % MOD)