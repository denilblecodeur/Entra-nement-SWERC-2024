# https://codeforces.com/gym/102501/problem/A
import sys
input = sys.stdin.buffer.readline
from heapq import *
import math
inf = 1<<59

xs, ys = map(int,input().split())
xd, yd = map(int,input().split())
B = int(input())
C = [int(input())]
T = int(input())
C.extend([int(input()) for _ in range(T)])
N = int(input())

pos = []
src, dest = N, N+1
graph = [[] for _ in range(N+2)]
graph[src].append((dest, 0))
for i in range(N):
    x, y, l, *nei = map(int,input().split())
    pos.append((x, y))
    graph[src].append((i, 0))
    graph[i].append((dest, 0))
    for li in range(l):
        j, m = nei[li<<1], nei[li<<1|1]
        graph[i].append((j, m))
        graph[j].append((i, m))
pos.extend((xs, ys))
pos.extend((xd, yd))
N += 2

DIST = [0] * N * N
for i in range(N):
    for j in range(i):
        DIST[i*N+j] = DIST[j*N+i] = math.ceil(math.dist(pos[i], pos[j]))

dp = [[inf] * (B+1) for _ in range(N)]
Q = [(0, 0, src)]
while Q:
    cost, km, v = heappop(Q)
    if v == dest:
        print(cost)
        break
    for u, mode in graph[v]:
        d = DIST[v*N+u]
        if km+d > B:
            continue
        new = cost + d * C[mode]
        if new < dp[u][km+d]:
            dp[u][km+d] = new
            heappush(Q, (new, km + d, u))
else:
    print(-1)