# https://www.acmicpc.net/problem/15408

import sys
input = sys.stdin.readline

n, k = map(int,input().split())
vtx = {}
edges = []
for _ in range(n):
    t, a, b, w = input().split()
    if a not in vtx: vtx[a] = len(vtx)+1
    if b not in vtx: vtx[b] = len(vtx)+1
    if t == 'BEF':
        edges.append((vtx[b], vtx[a], -int(w)))
    else:
        edges.append((vtx[b], vtx[a], int(w)))
        edges.append((vtx[a], vtx[b], int(w)))
N = len(vtx)+1
for vtx in range(1, N):
    edges.append((0, vtx, 0))

D = [1<<59] * N
D[0] = 0
for _ in range(N + 1):
    changed = False
    for node, neigh, weight in edges:
        if D[node] + weight < D[neigh]:
            D[neigh] = D[node] + weight
            changed = True
            
print('NO' if changed or -min(D) > k else 'YES')