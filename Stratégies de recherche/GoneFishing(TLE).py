import sys
input = sys.stdin.buffer.readline

ans = []
while True:
    n = int(input())
    if n == 0: break
    h = int(input())
    f = list(map(int,input().split()))
    d = list(map(int,input().split()))
    trs = list(map(int,input().split()))
    prev = [[0] * 200 for _ in range(n)]
    dp = [[-1] * 200 for _ in range(n)]
    dp[0][0] = 0
    bi, bt = 0, 0
    sum_trs = 0
    for i in range(n):
        if i>0:
            sum_trs += trs[i-1]
        for t in range(sum_trs, h * 12 + 1):
            fish, nb = 0, f[i]
            for ts in range(t - sum_trs + 1):
                if i == 0:
                    dp[i][t] = max(dp[i][t], fish)
                elif dp[i-1][t - ts - trs[i-1]] + fish > dp[i][t]:
                        dp[i][t] = dp[i-1][t - ts - trs[i-1]] + fish
                        prev[i][t] = t - ts - trs[i-1]
                fish += nb
                nb = max(nb - d[i], 0)
            if dp[i][t] > dp[bi][bt]:
                bi, bt = i, t

    t, left = bt, h * 12 - bt
    time = [0] * (n - 1 - bi)
    for i in reversed(range(1, bi + 1)):
        time.append((t - prev[i][t] - trs[i-1]) * 5)
        t = prev[i][t]
    time.append((t + left) * 5)

    ans.append(
        ', '.join(map(str, time[::-1]))
        + '\n' +
        "Number of fish expected: {}".format(dp[bi][bt])
    )

print("\n\n".join(ans))