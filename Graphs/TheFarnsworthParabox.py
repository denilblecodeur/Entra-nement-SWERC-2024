import sys
input = sys.stdin.buffer.readline

while True:
    n, b = map(int,input().split())
    if n == b == 0: break
    adj = [[None] * (n+1) for _ in range(n+1)]
    for _ in range(b):
        i, j, t = map(int,input().split())
        adj[i][j] = t
        adj[j][i] = -t
    seen = [None] * (n+1)
    Q = [(1, 0)]
    ans = False
    while Q:
        v, time = Q.pop()
        if seen[v] != None:
            ans |= seen[v] - time != 0
            continue
        seen[v] = time
        for u in range(1, n+1):
            if adj[v][u] != None and seen[u] is None:
                Q.append((u, time + adj[v][u]))
    print("Y" if ans else "N")