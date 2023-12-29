# https://www.beecrowd.com.br/judge/en/problems/view/2910
import sys
input = sys.stdin.buffer.readline
from heapq import *
inf = 1<<59

n, m = map(int,input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, l, c = map(int,input().split())
    a-=1;b-=1
    graph[a].append((b, l, c))
    graph[b].append((a, l, c))

dist = [inf] * n
dist[0] = 0
Q = [(0, 0)]
while Q:
    d, v = heappop(Q)
    for u, l, c in graph[v]:
        if dist[u] > d + l:
            dist[u] = d + l
            heappush(Q, (d+l, u))

edges = [inf] * n
for v in range(n):
    for u, l, c in graph[v]:
        if dist[v] + l == dist[u]:
            edges[u] = min(edges[u], c)
ans = 0
for v in range(n):
    if edges[v] != inf:
        ans += edges[v]
print(ans)