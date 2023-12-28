#include <bits/stdc++.h>
#define endl '\n'
#define fastio ios::sync_with_stdio(false), cout.tie(nullptr), cin.tie(nullptr);
using namespace std;
using pii = pair<int, int>;

const int lim = 10;
const int N = 500005;
int n, m, q, st, dist[N];

int main() {
    fastio;
    cin >> n >> m >> q;
    vector<vector<pii>> adj(n, vector<pii>());
    for (int i = 0; i < m; i++) {
        int u, v, w; cin >> u >> v >> w;
        if(u != v){
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
    }
    for(; q>0; q--){
        // dial's algorithm
        fill(dist, dist + n + 1, -1);
        cin >> st;
        dist[st] = 0;
        vector<vector<int>> Qs(lim + 1);
        Qs[0].push_back(st);
        for (int d = 0, mx = 0; d <= mx; d++) {
            for (auto& Q = Qs[d % (lim + 1)]; Q.size();) {
                int cur = Q.back(); Q.pop_back();
                if (dist[cur] != d) continue;
                for (const auto& [nxt, cost] : adj[cur]) {
                    if (dist[nxt] == -1 || dist[nxt] > d + cost) {
                        dist[nxt] = d + cost;
                        Qs[dist[nxt] % (lim + 1)].push_back(nxt);
                        mx = max(mx, dist[nxt]);
                    }
                }
            }
        }
        int far = *max_element(dist, dist + n + 1);
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if(dist[i] == far) cnt++;
        }
        cout << far << " " << cnt << endl;
    }
}