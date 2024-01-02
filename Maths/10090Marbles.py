# https://vjudge.net/problem/UVA-10090/origin

def bezout(a, b):
    px, py = 1, 0
    x, y = 0, 1
    while b != 0:
        a, (q, b) = b, divmod(a, b)
        px, x = x, px - q * x
        py, y = y, py - q * y
    return a, px, py

def solve(c1, n1, c2, n2):
    g, x, y = bezout(n1, n2)
    if n % g:
        return -1
    x *= n // g
    y *= n // g
    n1 //= g
    n2 //= g
    lo = -(x // n2)
    hi = y // n1
    if lo > hi:
        return -1
    res1 = c1 * (x + n2 * lo) + c2 * (y - n1 * lo)
    res2 = c1 * (x + n2 * hi) + c2 * (y - n1 * hi)
    if res1 < res2:
        return x + n2 * lo, y - n1 * lo
    return x + n2 * hi, y - n1 * hi

while True:
    n = int(input())
    if n == 0: break
    c1, n1 = map(int,input().split())
    c2, n2 = map(int,input().split())
    if n1 == 0 or n2 == 0:
        if n1 == n2 == 0 or n % max(n1, n2) != 0:
            print("failed")
        else:
            if n1 == 0:
                print(0, n // n2)
            else:
                print(n // n1, 0)
    elif n % n1 == n % n2 == 0:
        if c1 * (n // n1) < c2 * (n // n2):
            print(n // n1, 0)
        else:
            print(0, n // n2)
    else:
        ans = solve(c1, n1, c2, n2)
        if ans == -1:
            print('failed')
        else:
            print(*ans)