// https://www.spoj.com/problems/DISGRAPH/

#include <bits/stdc++.h>
#define endl '\n'
#define fastio ios::sync_with_stdio(false), cout.tie(nullptr), cin.tie(nullptr);
using namespace std;
typedef vector<int> VI;
typedef vector<VI> VVI;
const int INF = 1000000000;

pair<int, VI> GetMinCut(VVI &weights) {
  int N = weights.size();
  VI used(N), cut, best_cut;
  int best_weight = -1;
  
  for (int phase = N-1; phase >= 0; phase--) {
    VI w = weights[0];
    VI added = used;
    int prev, last = 0;
    for (int i = 0; i < phase; i++) {
      prev = last;
      last = -1;
      for (int j = 1; j < N; j++)
	if (!added[j] && (last == -1 || w[j] > w[last])) last = j;
      if (i == phase-1) {
	for (int j = 0; j < N; j++) weights[prev][j] += weights[last][j];
	for (int j = 0; j < N; j++) weights[j][prev] = weights[prev][j];
	used[last] = true;
	cut.push_back(last);
	if (best_weight == -1 || w[last] < best_weight) {
	  best_cut = cut;
	  best_weight = w[last];
	}
      } else {
	for (int j = 0; j < N; j++)
	  w[j] += weights[last][j];
	added[last] = true;
      }
    }
  }
  return make_pair(best_weight, best_cut);
}

int main(){
    int n; cin >> n;
    getchar();
    VVI weights(n, VI(n));
    for(int i=0; i<n; i++){
        string line, j;
        getline(cin, line);
        stringstream X(line);
        while (getline(X, j, ' ')){
            int nei = stoi(j);
            weights[i][nei] = weights[nei][i] = 1;
        }
    }
    pair<int, VI> res = GetMinCut(weights);
    cout << res.first << endl;
}