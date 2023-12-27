#include <bits/stdc++.h>
#define endl '\n'
#define fastio ios::sync_with_stdio(false), cout.tie(nullptr), cin.tie(nullptr);
using namespace std;

int n, h;
int f[30], d[30], trs[30];
int dp[30][200], pre[30][200];

void solve(){
    for(int i=0; i<n; i++){
        fill(dp[i], dp[i] + 200, -1);
        fill(pre[i], pre[i] + 200, 0);
    }
    dp[0][0] = 0;
    int bi=0, bt=0;
    int sum_trs = 0;
    for(int i=0; i<n; i++){
        if(i>0) sum_trs += trs[i-1];
        for(int t=sum_trs; t<=h*12; t++){
            int fish = 0, nb = f[i];
            for(int ts=0; ts<=t-sum_trs; ts++){
                if(i==0){ dp[i][t] = max(dp[i][t], fish); }
                else if(dp[i-1][t - ts - trs[i-1]] + fish > dp[i][t]){
                    dp[i][t] = dp[i-1][t - ts - trs[i-1]] + fish;
                    pre[i][t] = t - ts - trs[i-1];
                }
                fish += nb;
                nb = max(nb - d[i], 0);
            }
            if(dp[i][t] > dp[bi][bt]){ bi = i; bt = t; }
        }
    }
    int t = bt, left = h * 12 - bt;
    vector<int> time(n - 1 - bi, 0);
    for(int i=bi; i>0; i--){
        time.push_back((t - pre[i][t] - trs[i-1]) * 5);
        t = pre[i][t];
    }
    time.push_back((t + left) * 5);
    reverse(time.begin(), time.end());
    for(auto it = time.begin(); it != time.end(); it++){
        cout << *it;
        if(next(it) == time.end()) cout << endl;
        else cout << ", ";
    }
    cout << "Number of fish expected: " << dp[bi][bt] << endl;
}

int main(){
    fastio;
    cin >> n;
    while(n != 0){
        cin >> h;
        for(int i=0; i<n; i++) cin >> f[i];
        for(int i=0; i<n; i++) cin >> d[i];
        for(int i=0; i<n-1; i++) cin >> trs[i];
        solve();
        cin >> n;
        if(n != 0) cout << endl;
    }
}