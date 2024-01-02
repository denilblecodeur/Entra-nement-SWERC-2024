# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=697

import math

def crt(a, n):
    x = 0
    p = math.prod(n)
    for ai, ni in zip(a, n):
        xi = p // ni
        try: inv = pow(xi, -1, ni)
        except ValueError: return None
        x += ai * xi * inv
    return x % p

tc = 1
while True:
    p, e, i, d = map(int,input().split())
    if p == -1: break
    ans = crt([p, e, i], [23, 28, 33]) - d
    if ans <= 0:
        ans += 23 * 28 * 33
    print("Case {}: the next triple peak occurs in {} days.".format(tc, ans))
    tc += 1