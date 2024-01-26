# https://codeforces.com/contest/78/problem/E

from collections import deque
INF = 1<<59

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

n, t = map(int,input().split())
people = [input() for _ in range(n)]
input()
capsule = [input() for _ in range(n)]
time = [[-1] * n for _ in range(n)]
start = None
P, C = [], []
for i in range(n):
    if 'Z' in capsule[i]:
        j = capsule[i].find('Z')
        start = (i, j)
        time[i][j] = 0
    for j in range(n):
        if people[i][j] not in 'YZ0': P.append((i, j))
        if capsule[i][j] not in 'YZ0': C.append((i, j))

Q = deque([(*start, 0)])
while Q:
    i, j, d = Q.popleft()
    for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
        if 0<=i+di<n and 0<=j+dj<n and\
        capsule[i+di][j+dj] not in 'YZ' and\
        time[i+di][j+dj] == -1:
            time[i+di][j+dj] = min(d+1, t)
            Q.append((i+di, j+dj, d+1))

nP, nC = len(P), len(C)
N = nP + nC + 2
source, target = 0, N-1
graph = [{} for _ in range(N)]
for k, (i, j) in enumerate(P):
    add_edge(source, k + 1, int(people[i][j]))
for k, (i, j) in enumerate(C):
    add_edge(nP + k + 1, target, int(capsule[i][j]))

for i in range(n):
    for j in range(n):
        if capsule[i][j] not in 'YZ' and time[i][j] == -1:
            time[i][j] = t

_map = {tup:i for i, tup in enumerate(C)}

for k, tup in enumerate(P):
    Q = deque([(*tup, 0)])
    seen = [[False] * n for _ in range(n)]
    seen[tup[0]][tup[1]] = True
    while Q:
        i, j, d = Q.popleft()
        if (i, j) in _map:
            add_edge(k + 1, nP + _map[(i, j)] + 1, INF)
        if d == -1:
            continue
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if not(0<=i+di<n and 0<=j+dj<n) or capsule[i+di][j+dj] in 'YZ':
                continue
            if time[i+di][j+dj] >= d+1 and not seen[i+di][j+dj]:
                seen[i+di][j+dj] = True
                if time[i+di][j+dj] == d+1:
                    Q.append((i+di, j+dj, -1))
                else:
                    Q.append((i+di, j+dj, d+1))

_, maxflow = dinic(source, target, graph)
print(maxflow)