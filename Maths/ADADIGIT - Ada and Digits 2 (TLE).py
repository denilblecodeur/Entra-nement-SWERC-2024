# https://www.spoj.com/problems/ADADIGIT/

from itertools import permutations
from random import randrange, randint
from math import gcd

def is_prime(n):
    if n == 2: return 1
    if n == 1 or n%2 == 0: return 0
    m = n - 1
    lsb = m & -m
    s, d = lsb.bit_length()-1, m // lsb
    if n < 4759123141: test_numbers = [2, 7, 61]
    elif n < 341550071728321: test_numbers = [2, 3, 5, 7, 11, 13, 17]
    elif n < 3825123056546413051: test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    else: test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in test_numbers:
        if a == n: continue
        r, x = 0, pow(a,d,n)
        if x == 1: continue
        while x != m:
            x = pow(x,2,n)
            r += 1
            if x == 1 or r == s: return 0
    return 1

def find_prime_factor(n):
    m = max(1,int(n**0.125))
    while True:
        c = randrange(n)
        y = k = 0
        g = q = r = 1
        while g == 1:
            x, mr = y, 3*r//4
            while k < mr:
                y = (pow(y,2,n)+c)%n
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = (pow(y,2,n)+c)%n
                    q = q*abs(x-y)%n
                g = gcd(q,n)
                k += m
            k = r
            r <<= 1
        if g == n:
            g, y = 1, ys
            while g == 1:
                y = (pow(y,2,n)+c)%n
                g = gcd(abs(x-y),n)
        if g == n: continue
        if is_prime(g): return g
        elif is_prime(n//g): return n//g
        return find_prime_factor(g)

cache = {}

def update(cached_nb, cached_sm, cached_n, nb=0, sm=1):
    cached_n.reverse(); cached_nb.reverse(); cached_sm.reverse()
    for cnb, csm, cn in zip(cached_nb, cached_sm, cached_n):
        nb += cnb
        sm *= csm
        assert cn not in cache
        cache[cn] = (nb, sm)
    return nb, sm

def solve(n):
    nb, sm = 0, 1
    cached_nb, cached_sm, cached_n = [], [], []
    for p in range(2, 1000):
        if p*p > n: break
        if n%p: continue
        if n in cache:
            cnb, csm = cache[n]
            return update(cached_nb, cached_sm, cached_n, nb + cnb, sm * csm)
        cached_n.append(n)
        s = 0
        while n%p == 0:
            n //= p
            s += 1
        nb += s+1
        sm *= (pow(p, s+1) - 1) // (p - 1)
        cached_nb.append(s+1)
        cached_sm.append((pow(p, s+1) - 1) // (p - 1))
    while not is_prime(n) and n > 1:
        if n in cache:
            cnb, csm = cache[n]
            return update(cached_nb, cached_sm, cached_n, nb + cnb, sm * csm)
        cached_n.append(n)
        p = find_prime_factor(n)
        s = 0
        while n%p == 0:
            n //= p
            s += 1
        nb += s+1
        sm *= (pow(p, s+1) - 1) // (p - 1)
        cached_nb.append(s+1)
        cached_sm.append((pow(p, s+1) - 1) // (p - 1))
        if n != 1:
            if n in cache:
                cnb, csm = cache[n]
                return update(cached_nb, cached_sm, cached_n, nb + cnb, sm * csm)
            cached_n.append(n)
            nb += 2
            sm *= (n*n - 1) // (n - 1)
            cached_nb.append(2)
            cached_sm.append((n*n - 1) // (n - 1))
    return update(cached_nb, cached_sm, cached_n)

n = int(input())
a = sorted(input().split())

best_div = (0, -1)
best_sum = (0, -1)

for p in permutations(a):
    m = int(''.join(p))
    nb, sm = solve(m)
    if nb > best_div[1]:
        best_div = (m, nb)
    if sm > best_sum[1]:
        best_sum = (m, sm)

print(best_div[0], best_sum[0])