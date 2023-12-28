# https://codeforces.com/gym/102465/problem/D

from statistics import median

X, Y = map(int,input().split())
n = int(input())
dic = {}

for _ in range(n):
    x, y = map(int,input().split())
    if x not in dic:
        dic[x] = []
    dic[x].append(y)

pos = []
for x in dic:
    a, b = min(dic[x]), max(dic[x])
    pos.append(a)
    pos.append(b)

m = round(median(pos))

ans = X - 1
for x in dic:
    a, b = min(dic[x]), max(dic[x])
    if a >= m:
        ans += (b - m) * 2
    elif b <= m:
        ans += (m - a) * 2
    else:
        ans += (b - m) * 2
        ans += (m - a) * 2

print(int(ans))