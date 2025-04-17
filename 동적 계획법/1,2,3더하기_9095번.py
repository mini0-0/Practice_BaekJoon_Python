import sys
input = sys.stdin.readline

T = int(input())
t_list = [int(input()) for i in range(T)]

dp = [0] * 11
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for t in t_list:
    print(dp[t])