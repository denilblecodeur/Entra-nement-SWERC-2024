# https://codeforces.com/gym/101845/problem/C
import sys
input = sys.stdin.readline

a = input().rstrip('\n')
b = input().rstrip('\n')

dp = [[-1] * 100 for _ in range(100)]
for _ in range(int(input())):
    x, y, c = input().split()
    x, y, c = ord(x)-33, ord(y)-33, int(c)
    dp[x][y] = c if dp[x][y] == -1 else min(dp[x][y], c)

for x in range(100):
    dp[x][x] = 0

for k in range(100):
    for i in range(100):
        if dp[i][k] == -1: continue
        for j in range(100):
            if dp[k][j] == -1: continue
            if dp[i][j] == -1 or dp[i][j] > dp[i][k] + dp[k][j]:
                dp[i][j] = dp[i][k] + dp[k][j]

ans = 0
for x, y in zip(a, b):
    x, y = ord(x)-33, ord(y)-33
    if dp[x][y] == -1:
        ans = -1
        break
    ans += dp[x][y]
print(ans)