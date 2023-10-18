#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"

void solve() {
    int m, max_index = -1, current_index = 0;
    string s, l, r;
    cin >> s >> m >> l >> r;
    for (int i = 0; i < m; i++) {
        int next = max_index + 1;
        for (int c = l[i]; c <= r[i]; c++) {
            current_index = s.find(c, next);
            if (current_index == -1) {
                cout << "YES" << endl;
                return;
            }
            max_index = max(max_index, current_index);
        }
    }
    cout << "NO" << endl;
}

int main() {
    ios;
    
    #ifndef ONLINE_JUDGE
    freopen(input_file, "r", stdin);
    freopen(output_file, "w", stdout);
    #endif

    ll num_test_cases;
    cin >> num_test_cases;
    while(num_test_cases--) {
        solve();
    }
    return 0;
}
