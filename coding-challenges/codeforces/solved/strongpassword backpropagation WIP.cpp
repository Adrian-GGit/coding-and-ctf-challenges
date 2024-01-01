#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"


tuple<ll, bool> get_next_index(string s, ll current_index, ll current_li, ll current_ri) {
    ll index = current_index, left = 0, right = 0;
    bool l_interrupt = false, r_interrupt = false;
    ll current_char = -1;
    bool interrupt = false;
    while (index < s.length()) {
        current_char = s[index] - '0';
        if (current_li <= current_char && current_char <= current_ri) {
            index++;
            interrupt = true;
            break;
        } else {
            index++;
        }
    }
    if (index < s.length()) {
        if (current_li <= current_char - 1) {
            tie(left, l_interrupt) = get_next_index(s, index, current_li, current_char - 1);
        }
        if (current_char + 1 <= current_ri) {
            tie(right, r_interrupt) = get_next_index(s, index, current_char + 1, current_ri);
        }
    }
    // cout << current_li << " " << current_ri << " " << index << " " << left << " " << right << " | interrupt: " << interrupt << " " << l_interrupt << " " << r_interrupt << endl;
    ll next_index = max({index, left, right});
    bool ir;
    if (index == next_index) ir = interrupt;
    else if (left == next_index) ir = l_interrupt;
    else ir = r_interrupt;
    return make_tuple(next_index, ir);
}


main() {
    ios;
    
    #ifndef ONLINE_JUDGE
    freopen(input_file, "r", stdin);
    freopen(output_file, "w", stdout);
    #endif

    ll num_test_cases;
    cin >> num_test_cases;
    while(num_test_cases--) {
        ll m;
        string s, l, r;
        cin >> s >> m >> l >> r;
        ll password_index = 0, current_index = 0, current_li = l[password_index] - '0', current_ri = r[password_index] - '0';
        bool interrupt;
        while (current_index < s.length() && password_index < m) {
            tie(current_index, interrupt) = get_next_index(s, current_index, current_li, current_ri);
            cout << "current_index: " << current_index << " | interrupt: " << interrupt << endl;
            password_index++;
            current_li = l[password_index] - '0';
            current_ri = r[password_index] - '0';
        }
        cout << endl;
    }
}
