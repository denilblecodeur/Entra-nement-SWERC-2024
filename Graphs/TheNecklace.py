# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=995
import sys
input = sys.stdin.buffer.readline
from collections import deque

#Fleury’s Algorithm (fonctionne avec multigraph)
def get_eulerian_tour(edges, src):
    def get_next_node(node):
        current, degree = 0, 0
        for neigh, deg in enumerate(edges[node]):
            if deg > degree:
                current, degree = neigh, deg
        if degree > 0:
            edges[node][current] -= 1
            edges[current][node] -= 1
            return (node, current)
        else:
            return None
    _next = get_next_node(src[1])
    order = deque([_next])
    blocked = 0
    while blocked < n:
        _next = get_next_node(order[-1][1])
        if _next:
            order.append(_next)
            blocked = 0
        elif len(order) != n:
            prev = order.pop()
            order.appendleft(prev)
            blocked += 1
        else:
            break
    return order if len(order) == n else None

ans = []
for tc in range(int(input())):
    n = int(input())
    edges = [[0] * 51 for _ in range(51)]
    src, deg = None, 0
    for i in range(n):
        u, v = map(int,input().split())
        edges[u][v] += 1
        edges[v][u] += 1
        if i == 0: src = (u, v)
        deg ^= (1<<u) ^ (1<<v)
    if deg == 0:
        necklace = get_eulerian_tour(edges, src)
        if necklace is not None:
            ans.append("Case #{}\n".format(tc+1) + '\n'.join("{} {}".format(a, b) for a, b in necklace))
            continue
    ans.append("Case #{}\n".format(tc+1) + "some beads may be lost")

print('\n\n'.join(ans))