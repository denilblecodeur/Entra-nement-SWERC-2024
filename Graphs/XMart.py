# https://matcomgrader.com/problem/9440/x-mart/
import sys
input = sys.stdin.buffer.readline

def tarjan(G):
    n = len(G)
    SCC, S, P = [], [], []
    Q, state = list(range(n)), [0] * n
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
    return SCC

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

while True:
    n, p = map(int,input().split())
    if n == p == 0: break
    ts = TwoSat(p+1)
    for _ in range(n):
        x, y, s, t = map(int,input().split())
        if not(x == y == 0):
            if x == 0: ts.set(y)
            elif y == 0: ts.set(x)
            else: ts.either(x, y)
        if not(s == t == 0):
            if s == 0: ts.set(~t)
            elif t == 0: ts.set(~s)
            else: ts.either(~s, ~t)
    ok, sol = ts.solve()
    print("yes" if ok else "no")