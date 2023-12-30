# https://codeforces.com/contest/1202/problem/B
import sys
input = sys.stdin.readline

dp = [[[101] * 10 for _ in range(10)] for _ in range(11)]

for i in range(11):
    for d in range(i, 100, 10):
        for x in range(10):
            for y in range(x + 1):
                if i == 0:
                    if min(x, y) == 0:
                        dp[i][y][x] = dp[i][x][y] = 1
                    continue
                if x == y:
                    if x != 0 and d % x == 0:
                        if dp[i][x][y] > d // x:
                            dp[i][y][x] = dp[i][x][y] = d // x
                elif y == 0:
                    if d % x == 0:
                        if dp[i][x][y] > d // x:
                            dp[i][y][x] = dp[i][x][y] = d // x
                else:
                    for k in range(d // x + 1):
                        if (d - x * k) % y == 0:
                            if dp[i][x][y] > k + (d - x * k) // y:
                                dp[i][y][x] = dp[i][x][y] = k + (d - x * k) // y

s = list(map(int,input().rstrip('\n')))

diff = [[0] * 10 for _ in range(10)]
for i in range(len(s) - 1):
    diff[s[i]][s[i+1]] += 1

ans = [[-1] * 10 for _ in range(10)]
for x in range(10):
    for y in range(x + 1):
        cnt = 0
        good = True
        for a in range(10):
            for b in range(10):
                if diff[a][b] == 0:
                    continue
                d = (b - a) % 10
                if d == 0:
                    good &= min(dp[0][x][y], dp[10][x][y]) < 101
                    cnt += diff[a][b] * (min(dp[0][x][y], dp[10][x][y])-1)
                else:
                    good &= dp[d][x][y] < 101
                    cnt += diff[a][b] * (dp[d][x][y]-1)
                if not good: break
            if not good: break
        else:
            ans[x][y] = ans[y][x] = cnt

for i in range(10):
    print(*ans[i])