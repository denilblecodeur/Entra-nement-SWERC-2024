# https://codeforces.com/gym/102006/problem/D
import sys
sys.stdin = open("balls.in", "r")
input = sys.stdin.readline

for _ in range(int(input())):
    R, C = map(int,input().split())
    b = list(map(int,input().split()))
    grid = [input().rstrip('\n') for _ in range(R)]
    s = list(map(int,input().split()))

    cur = [0] + s + [0]
    for i in reversed(range(R)):
        nex = [0] * (C + 2)
        for j in range(C):
            nex[j+1] = cur[j+1]
            if grid[i][j] != '.':
                nex[j+1] = max(cur[j], cur[j+1], cur[j+2])
        cur = nex

    ans = 0
    for i, bi in enumerate(b, 1):
        ans += bi * cur[i]
    print(ans)