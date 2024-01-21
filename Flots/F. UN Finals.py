# https://codeforces.com/gym/101845/problem/F

from collections import deque

def dinic(source, target, graph):
    def _dinic_step(lev, u, t, limit):
        if limit <= 0: return 0
        if u == t: return limit
        val = 0
        for v in graph[u]:
            residuel = graph[u][v] - flow[u][v]
            if lev[v] == lev[u] + 1 and residuel > 0:
                z = min(limit, residuel)
                aug = _dinic_step(lev, v, t, z)
                flow[u][v] += aug
                flow[v][u] -= aug
                val += aug
                limit -= aug
        if val == 0: lev[u] = None
        return val
    n = len(graph)
    Q = deque()
    total = 0
    flow = [[0] * n for _ in range(n)]
    while True:
        Q.appendleft(source)
        lev = [None] * n
        lev[source] = 0
        while Q:
            u = Q.pop()
            for v in graph[u]:
                if lev[v] is None and graph[u][v] > flow[u][v]:
                    lev[v] = lev[u] + 1
                    Q.appendleft(v)
        if lev[target] is None: break
        UB = sum(graph[source][v] for v in graph[source]) - total
        total += _dinic_step(lev, source, target, UB)
    return flow, total

def add_edge(u, v, c):
    if v not in graph[u]:
        graph[u][v] = 0
        graph[v][u] = 0
    graph[u][v] += c

n = int(input())
N = n + 28
graph = [{} for _ in range(N)]
for i in range(1, n+1):
    add_edge(0, i, 1)
    career = [0] * 26
    for grp in input().split():
        for char in grp:
            career[ord(char) - 65] += 1
    m = max(career)
    for char in range(26):
        if career[char] == m:
            add_edge(i, n + char + 1, 1)
k = int(input())
for char in range(26):
    add_edge(n + char + 1, N - 1, k)

_, maxflow = dinic(0, N - 1, graph)
print(maxflow)