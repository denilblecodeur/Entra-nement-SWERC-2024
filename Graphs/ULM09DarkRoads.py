# https://www.spoj.com/problems/ULM09/
import sys
input = sys.stdin.buffer.readline

class DSU:
    def __init__(self, n):
        self.up = list(range(n))
        self.size = [1] * n
    def find(self, x):
        if self.up[x] != x:
            self.up[x] = self.find(self.up[x])
        return self.up[x]
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.up[y] = x
        self.size[x] += self.size[y]
        return True

while True:
    n, m = map(int,input().split())
    if n == m == 0: break
    edges = [tuple(map(int,input().split())) for _ in range(m)]
    edges.sort(key=lambda t:t[2])
    dsu = DSU(n + 1)
    ans = 0
    for x, y, z in edges:
        if not dsu.union(x, y):
            ans += z
    print(ans)