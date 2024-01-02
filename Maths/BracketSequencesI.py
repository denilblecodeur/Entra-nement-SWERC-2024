# https://cses.fi/problemset/result/5384486/

def catalan(n, mod):
    x = 1
    for k in range(2, n + 1):
        x *= (1 + n * pow(k, -1, mod)) % mod
        x %= mod
    return x

mod = 10**9+7
n = int(input())
print(0 if n % 2 else catalan(n // 2, 10**9+7))