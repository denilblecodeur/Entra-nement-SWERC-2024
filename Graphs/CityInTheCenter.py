# https://www.beecrowd.com.br/judge/en/problems/view/2676
import sys
input = sys.stdin.buffer.readline

while True:
    n, m = map(int,input().split())
    if n == m == 0: break
    dist = [[-1] * n for _ in range(n)]
    for _ in range(m):
        u, v, d = map(int,input().split())
        u-=1;v-=1
        if dist[u][v] == -1 or dist[u][v] > d:
            dist[v][u] = dist[u][v] = d
    for v in range(n):
        dist[v][v] = 0
    for k in range(n):
        for i in range(n):
            if dist[i][k] == -1: continue
            for j in range(n):
                if dist[k][j] == -1: continue
                if dist[i][j] == -1 or dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    best = min(sum(dist[v]) for v in range(n))
    ans = []
    for v in range(n):
        if sum(dist[v]) == best:
            print(v+1, end=' ')
    print()