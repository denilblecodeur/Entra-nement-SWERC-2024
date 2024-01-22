# https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1421

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

def mincut(source, target, graph):
    flow, _ = dinic(source, target, graph)
    reachable = set([source])
    Q = [source]
    seen = set()
    while Q:
        u = Q.pop()
        seen.add(u)
        for v in graph[u]:
            if v not in seen and graph[u][v] > flow[u][v]:
                reachable.add(v)
                Q.append(v)
    cut = []
    for u in reachable:
        for v in graph[u]:
            if v not in reachable:
                cut.append((u, v))
    return cut

while True:
    n, m = map(int,input().split())
    if n == m == 0: break
    graph = [{} for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int,input().split())
        add_edge(u-1, v-1, w)
        add_edge(v-1, u-1, w)
    ans = mincut(0, 1, graph)
    for u, v in ans:
        print(u+1, v+1)
    print()