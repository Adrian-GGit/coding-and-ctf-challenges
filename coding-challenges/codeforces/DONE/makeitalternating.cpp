#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"


ll mod = 998244353;

ll fak(ll n) {
    return (n == 0) || (n == 1) ? 1 : ((n % mod) * (fak(n - 1) % mod) % mod);
}

main() {
    ios;

    #ifndef ONLINE_JUDGE
    freopen(input_file, "r", stdin);
    freopen(output_file, "w", stdout);
    #endif

    ll num_test_cases, current_len_of_seq;
    ll min_num_ops, num_shortest_seq, len_current_seq, num_combs; 
    string s, next_needed;
    cin >> num_test_cases;
    while(num_test_cases--) {
        min_num_ops = 0, num_shortest_seq = 0, len_current_seq = 1, num_combs = 1;
        cin >> s;
        char current_char, previous_char = s[0];
        for (ll i = 1; i < s.length(); i++) {
            current_char = s[i];
            if (previous_char == current_char) {
                min_num_ops += 1;
                len_current_seq += 1;
            } else {
                previous_char = current_char;
                num_combs = ((num_combs % mod) * (len_current_seq % mod)) % mod;
                len_current_seq = 1;
            }
        }
        num_combs = ((num_combs % mod) * (len_current_seq % mod)) % mod;
        num_shortest_seq = ((num_combs % mod) * (fak(min_num_ops) % mod)) % mod;
        cout << min_num_ops << " " << num_shortest_seq << endl;
    }
}
