# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1249
import sys
lines = sys.stdin.read()
if lines[-1] != '\n': lines += '\n'

def solve():
    Q = [(1, 0, 0)]
    far, maxd = 1, 0
    while Q:
        v, par, d = Q.pop()
        if d > maxd:
            far, maxd = v, d
        for u, w in graph[v]:
            if u != par:
                Q.append((u, v, d+w))
    Q = [(far, 0, 0)]
    ans = -1
    while Q:
        v, par, d = Q.pop()
        ans = max(ans, d)
        for u, w in graph[v]:
            if u != par:
                Q.append((u, v, d+w))
    print(ans)

n = 10001
graph = [[] for _ in range(n)]

for line in lines.split('\n'):
    if line == '':
        solve()
        graph = [[] for _ in range(n)]
    else:
        u, v, w = map(int, line.split())
        graph[u].append((v, w))
        graph[v].append((u, w))