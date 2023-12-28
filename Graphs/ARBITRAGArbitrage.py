# https://www.spoj.com/problems/ARBITRAG/
import sys
input = sys.stdin.readline

tc = 1
while True:
    n = int(input())
    if n == 0: break
    cur = dict(
        zip([input().rstrip('\n') for _ in range(n)], range(n))
        )

    dist = [[0] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 1
    for _ in range(int(input())):
        ci, rate, cj = input().split()
        dist[cur[ci]][cur[cj]] = float(rate)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = max(dist[i][j], dist[i][k] * dist[k][j])

    for i in range(n):
        if dist[i][i] > 1:
            print("Case {}: Yes".format(tc))
            break
    else:
        print("Case {}: No".format(tc))
    
    input()
    tc += 1