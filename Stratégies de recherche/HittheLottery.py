n = int(input())
ans = 0
for bi in [1, 5, 10, 20, 100][::-1]:
    q, n = divmod(n, bi)
    ans += q
print(ans)