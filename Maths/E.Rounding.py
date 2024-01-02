# https://codeforces.com/gym/102465/problem/E

n = int(input())
places = {}

for _ in range(n):
    s, x = input().split()
    places[s] = int(x)

SUM_INF = sum(max(v - 0.5, 0) for v in places.values())
SUM_SUP = sum(min(v + 0.49, 100) for v in places.values())

if SUM_INF > 100 or SUM_SUP < 100:
    print("IMPOSSIBLE") & exit()

for k, v in places.items():
    lo = v - min((SUM_SUP - min(100 - v, 0.49)) - 100, 0.5)
    hi = v + min(100 - (SUM_INF + min(v, 0.5)), 0.49)
    print('{} {:.02f} {:.02f}'.format(k, max(lo, 0), min(hi, 100)))