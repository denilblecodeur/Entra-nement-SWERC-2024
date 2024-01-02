# https://vjudge.net/problem/UVA-10814/origin

import math

for _ in range(int(input())):
    a, b = input().split(' / ')
    g = math.gcd(int(a), int(b))
    print(int(a)//g, '/', int(b)//g)