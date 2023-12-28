# https://www.spoj.com/problems/LABYR1/en/
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    C, R = map(int,input().split())
    grid = [list(input().rstrip('\n')) for _ in range(R)]
    Q = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '.':
                Q.append((i, j, 0))
                break
        if Q: break
    fi, fj, maxd = Q[0]
    while Q:
        i, j, d = Q.pop()
        grid[i][j] = '+'
        if d > maxd:
            fi, fj, maxd = i, j, d
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if 0<=i+di<R and 0<=j+dj<C and grid[i+di][j+dj] == '.':
                Q.append((i+di, j+dj, d+1))
    Q = [(fi, fj, 0)]
    ans = 0
    while Q:
        i, j, d = Q.pop()
        grid[i][j] = '#'
        ans = max(ans, d)
        for di, dj in ((0,1),(1,0),(0,-1),(-1,0)):
            if 0<=i+di<R and 0<=j+dj<C and grid[i+di][j+dj] != '#':
                Q.append((i+di, j+dj, d+1))
    print("Maximum rope length is {}.".format(ans))