// https://codeforces.com/gym/101908/problem/G

#include <bits/stdc++.h>
#define endl '\n'
#define ll long long
#define fastio ios::sync_with_stdio(false), cout.tie(nullptr), cin.tie(nullptr);
using namespace std;

struct Dinic {
	struct Edge {
		int to, rev;
		ll c, oc;
		ll flow() { return max(oc - c, 0LL); } // if you need flows
	};
	vector<int> lvl, ptr, q;
	vector<vector<Edge>> adj;
	Dinic(int n) : lvl(n), ptr(n), q(n), adj(n) {}
	void addEdge(int a, int b, ll c, ll rcap = 0) {
		adj[a].push_back({b, int((adj[b]).size()), c, c});
		adj[b].push_back({a, int((adj[a]).size()) - 1, rcap, rcap});
	}
	ll dfs(int v, int t, ll f) {
		if (v == t || !f) return f;
		for (int& i = ptr[v]; i < int((adj[v]).size()); i++) {
			Edge& e = adj[v][i];
			if (lvl[e.to] == lvl[v] + 1)
				if (ll p = dfs(e.to, t, min(f, e.c))) {
					e.c -= p, adj[e.to][e.rev].c += p;
					return p;
				}
		}
		return 0;
	}
	ll calc(int s, int t) {
		ll flow = 0; q[0] = s;
        for(int L=0; L<31; L++){
            do {
                lvl = ptr = vector<int>(int((q).size()));
                int qi = 0, qe = lvl[s] = 1;
                while (qi < qe && !lvl[t]) {
                    int v = q[qi++];
                    for (Edge e : adj[v])
                        if (!lvl[e.to] && e.c >> (30 - L))
                            q[qe++] = e.to, lvl[e.to] = lvl[v] + 1;
                }
                while (ll p = dfs(s, t, LLONG_MAX)) flow += p;
            } while (lvl[t]);
        }
		return flow;
	}
	bool leftOfMinCut(int a) { return lvl[a] != 0; }
};

int main(){
    int P, R, C; cin >> P >> R >> C;
    vector<int> demands(P), stocks(R);
    vector<int> I(C), J(C), T(C);
    for(int i=0; i<P; i++) cin >> demands[i];
    for(int i=0; i<R; i++) cin >> stocks[i];
    for(int i=0; i<C; i++) cin >> I[i] >> J[i] >> T[i];
    ll goal = accumulate(demands.begin(), demands.end(), 0);
    int lo = 0, hi = 1e6+1;
    while(lo < hi){
        int x = (lo + hi) / 2;
        Dinic din = Dinic(P + R + 2);
        for(int j=1; j<=R; j++) din.addEdge(0, j, stocks[j-1]);
        for(int i=1; i<=P; i++) din.addEdge(R + i, P+R+1, demands[i-1]);
        for(int i=0; i<C; i++){
            if(T[i] <= x) din.addEdge(J[i], R+I[i], LLONG_MAX);
        }
        if(din.calc(0, P+R+1) == goal) hi = x;
        else lo = x + 1;
    }
    if(lo == 1e6+1) lo = -1;
    cout << lo << endl;
}