#include <bits/stdc++.h>
#define endl '\n'
#define ll long long
#define fastio ios::sync_with_stdio(false), cout.tie(nullptr), cin.tie(nullptr);
using namespace std;

const int inf = 1e9;

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
		adj[b].push_back({a, int((adj[a]).size()) - 1, c, c});
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

int mat[1005][1005];

int main(){
    fastio;
    int n; cin >> n;
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++) cin >> mat[i][j];
    }
    int N=n+1;
    Dinic din(N*N+2);
    int s = 0, t = N*N+1;
    for(int i=0; i<n; i++){
        din.addEdge(s, i+1, inf);
        din.addEdge(N*(N-1)+i+1, t, inf);
    }
    for(int x=1; x<t; x++){
        int i = (x-1)/N, j=(x-1)%N, c;
        // droite
        if(j < N-1){
            c = 0;
            if(i<n) c += mat[i][j];
            if(i>0) c += mat[i-1][j];
            din.addEdge(x, x+1, c);
        }
        // bas
        if(i < N-1){
            c = 0;
            if(j<n) c += mat[i][j];
            if(j>0) c += mat[i][j-1];
            din.addEdge(x, x+N, c);
        }
    }
    cout << din.calc(s, t) << endl;
}