# https://codeforces.com/problemset/problem/1472/B

for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    one = a.count(1)
    two = n - one
    if two % 2 == 0:
        print("YES" if one%2==0 else "NO")
    else:
        print("YES" if one>=2 and one%2==0 else "NO")