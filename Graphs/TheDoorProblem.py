# https://codeforces.com/contest/776/problem/D
import sys
input = sys.stdin.buffer.readline

def tarjan(G):
    SCC, S, P = [], [], []
    Q, state = list(range(len(G))), [0] * len(G)
    while Q:
        node = Q.pop()
        if node < 0:
            d = state[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:]; P.pop()
                for v in SCC[-1]:
                    state[v] = -1
        elif state[node] > 0:
            while P[-1] > state[node]:
                P.pop()
        elif state[node] == 0:
            S.append(node)
            P.append(len(S))
            state[node] = len(S)
            Q.append(~node)
            Q.extend(G[node])
    return SCC[::-1]
 
class TwoSat:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(2 * n)]
 
    def _imply(self, x, y):
        self.graph[x].append(y if y >= 0 else 2 * self.n + y)
 
    def either(self, x, y):
        """either x or y must be True"""
        self._imply(~x, y)
        self._imply(~y, x)
 
    def set(self, x):
        """x must be True"""
        self._imply(~x, x)
 
    def implies(self, x, y):
        self.either(~x, y)
 
    def solve(self):
        SCC = tarjan(self.graph)
        order = [0] * (2 * self.n)
        for i, comp in enumerate(SCC):
            for x in comp:
                order[x] = i
        for i in range(self.n):
            if order[i] == order[~i]:
                return False, None
        return True, [+(order[i] > order[~i]) for i in range(self.n)]

n, m = map(int,input().split())
status = list(map(int,input().split()))
switch = [set() for _ in range(n)]
for i in range(m):
    line = map(int,input().split())
    next(line)
    for x in line:
        switch[x-1].add(i+1)

ts = TwoSat(m+1)
for i, r in enumerate(status):
    a, b = switch[i]
    if r:
        ts.implies(a, b)
        ts.implies(b, a)
    else:
        ts.either(a, b)
        ts.either(~a, ~b)

ok, sol = ts.solve()
print("YES" if ok else "NO")