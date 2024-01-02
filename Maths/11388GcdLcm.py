# https://vjudge.net/problem/UVA-11388/origin

import math

for _ in range(int(input())):
    g, l = map(int,input().split())
    if math.lcm(g, l) == l:
        print(g, l)
    else:
        print(-1)