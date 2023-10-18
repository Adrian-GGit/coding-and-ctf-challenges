#include <cstdio>
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"

main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    #ifndef ONLINE_JUDGE
    freopen(input_file, "r", stdin);
    freopen(output_file, "w", stdout);
    freopen(output_file, "w", stdout);
    #endif

    ll num_test_cases;
    cin >> num_test_cases;
    while(num_test_cases--) {
        ll num_cols, max_water, left = 1, max_height = 1;
        cin >> num_cols >> max_water;
        vector<ll> coral_height(num_cols);
        for(ll i = 0 ; i < num_cols ; i++) {
            cin >> coral_height[i];
        }
        max_height = (max_water / num_cols) + *max_element(coral_height.begin(), coral_height.end());
        ll right = max_height + 1;
        while (left < right - 1) {
            ll amount_water = 0;
            ll mid_height = (left + right + 1) / 2;
            for (ll i = 0; i < num_cols; i++) {
                ll current_coral_height = coral_height[i];
                amount_water += current_coral_height < mid_height ? (mid_height - current_coral_height) : 0;
            }
            if (max_water < amount_water) {
                right = mid_height;
            } else {
                left = mid_height;
            }
        }
        cout << left << "\n";
    }
}
