#include <bits/stdc++.h>
using namespace std;

const int LIM = 1000002;
int nb_composite[LIM];

void sieve(){
    for(int i=2; i<LIM; i++){
        if(nb_composite[i] == 0){
            for(int j = i+i; j<LIM; j += i) nb_composite[j] = 1;
        }
        nb_composite[i] += nb_composite[i-1];
    }
}

int n, k;
int p[10];

int main(){
    sieve();
    int t; cin >> t;
    for(int tc=1; tc<=t; tc++){
        int n, k; cin >> n >> k;
        for(int i=0; i<k; i++) cin >> p[i];
        int ans = 0;
        for(int mask=1; mask<(1<<k); mask++){
            unsigned long long num = 1;
            for(int i=0; i<k; i++){
                if((mask>>i)&1) num *= p[i];
                if(num > n) break;
            }
            if(__builtin_popcount(mask)&1) ans += n / num;
            else ans -= n / num;
        }
        for(int i=0; i<k; i++) if(p[i] <= n){ ans--; }
        cout << "Case " << tc << ": " << nb_composite[n] - ans << endl;
    }
}