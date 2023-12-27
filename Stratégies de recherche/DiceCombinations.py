n = int(input())
dp = [0] * max(n+1, 7)
dp[0] = 1
for i in range(1, n+1):
    dp[i] = sum(dp[j] for j in range(max(i-6, 0), i)) % (10**9+7)
print(dp[n])