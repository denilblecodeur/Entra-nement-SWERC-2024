# https://cses.fi/problemset/task/1684
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
ts = TwoSat(m+1)
for _ in range(n):
    a, b, c, d = input().split()
    if a == b'+' and c == b'+':
        ts.either(int(b), int(d))
    if a == b'+' and c == b'-':
        ts.either(int(b), ~int(d))
    if a == b'-' and c == b'+':
        ts.either(~int(b), int(d))
    if a == b'-' and c == b'-':
        ts.either(~int(b), ~int(d))
ok, sol = ts.solve()
if not ok:
    print("IMPOSSIBLE") & exit()
for i in range(1, m+1):
    print("-+"[sol[i]], end=" \n"[i==m])