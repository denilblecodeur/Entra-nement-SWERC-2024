# https://codeforces.com/problemset/problem/633/A

import math

def bezout(a, b):
    # Calcule une solution à l’équation ax + by = pgcd(a, b)
    px, py = 1, 0
    x, y = 0, 1
    while b != 0:
        a, (q, b) = b, divmod(a, b)
        px, x = x, px - q * x
        py, y = y, py - q * y
    return a, px, py # pgcd, x, y

def solve(a, b, n):
    g, x, y = bezout(a, b)
    if n % g:
        return -1
    # to get to ax + by = n
    x *= n // g
    y *= n // g
    # two equations of Linear Diophantine x = x0 + (b/d)n, y = y0 - (a/d)n, where n is an integer
    # derivation of n based on the fact that x and y have to be positive
    # x0 + (b/d)n >= 0, solve for n: we get n >= -x0*d/b
    # y0 - (a/d)n >= 0, solve for n: we get n <= y0*d/a
    # putting together -x0*d/b <= n <= y0*d/a
    lo = -((x * g) // b)
    hi = (y * g) // a
    if lo > hi:
        return -1
    return x + (b * lo) // g, y - (a * lo) // g

a, b, c = map(int,input().split())
print("Yes" if solve(a, b, c) != -1 else "No")