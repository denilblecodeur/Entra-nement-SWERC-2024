#include <bits/stdc++.h>
#define MAXN 2050
using namespace std;

int n, x, y;
char grid[MAXN][MAXN];

void solve(int i, int j, int i_manq, int j_manq, char letter, int dim){
    if(dim == 1) return;
    if(dim == 2){
        grid[i][j] = letter;
        grid[i + 1][j] = letter;
        grid[i][j + 1] = letter;
        grid[i + 1][j + 1] = letter;
        grid[i_manq][j_manq] = 'E';
        return;
    }
    dim /= 2;
    int zone = i_manq < i + dim ? j_manq < j + dim ? 0 : 1 : j_manq < j + dim ? 2 : 3;

    if(zone != 0) solve(i, j, i + dim - 1, j + dim - 1, 'A', dim);
    else solve(i, j, i_manq, j_manq, 'A', dim);

    if(zone != 1) solve(i, j + dim, i + dim - 1, j + dim, 'B', dim);
    else solve(i, j + dim, i_manq, j_manq, 'B', dim);

    if(zone != 2) solve(i + dim, j, i + dim, j + dim - 1, 'C', dim);
    else solve(i + dim, j, i_manq, j_manq, 'C', dim);

    if(zone != 3) solve(i + dim, j + dim, i + dim, j + dim, 'D', dim);
    else solve(i + dim, j + dim, i_manq, j_manq, 'D', dim);
}

int main(){
    cin >> n;
    cin >> x >> y;
    solve(0, 0, x - 1, y - 1, 'X', n);
    grid[x - 1][y - 1] = '.';
    for(int i=0; i<n; i++){
        for(int j=0; j<n; j++){
            cout << grid[i][j];
        }
        cout << endl;
    }
    return 0;
}