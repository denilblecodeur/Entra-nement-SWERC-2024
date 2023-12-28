# https://www.urionlinejudge.com.br/judge/en/problems/view/1655
import sys
input = sys.stdin.buffer.readline

while True:
    line = input().split()
    if len(line) < 2: break
    n, m = map(int, line)
    graph = [{} for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int,input().split())
        u-=1;v-=1
        graph[u][v] = p/100
        graph[v][u] = p/100
    proba = [0] * n
    proba[0] = 1
    for _ in range(n + 1):
        for v in range(n):
            for u, p in graph[v].items():
                proba[u] = max(proba[u], proba[v] * p)
    print("{:.6f} percent".format(100 * proba[n-1]))