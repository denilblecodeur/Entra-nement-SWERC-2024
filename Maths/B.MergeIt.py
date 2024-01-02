# https://codeforces.com/problemset/problem/1176/B

for _ in range(int(input())):
    n = int(input())
    a = [int(x) % 3 for x in input().split()]
    two = a.count(2)
    one = a.count(1)
    print(a.count(0) + min(one, two) + abs(one - two) // 3)