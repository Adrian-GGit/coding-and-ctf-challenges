#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"

template <typename T>

tuple<T, T> cin_to_vector(vector<T> &vec) {
    T sum = 0;
    T min = -1;
    for (ll i = 0; i < vec.size(); i++) {
        cin >> vec[i];
        sum += vec[i];
        if (min == -1 or vec[i] < min) min = vec[i];
    }
    return make_tuple(sum, min);
}

main() {
    ios;
    
    #ifndef ONLINE_JUDGE
    freopen(input_file, "r", stdin);
    freopen(output_file, "w", stdout);
    #endif

    ll num_test_cases;
    cin >> num_test_cases;
    for (ll i = 0; i < num_test_cases; i++) {
        ll board_size;
        cin >> board_size;
        vector<ll> costs_y(board_size);
        ll sum_y, min_y;
        tie(sum_y, min_y) = cin_to_vector<ll>(costs_y);
        vector<ll> costs_x(board_size);
        ll sum_x, min_x;
        tie(sum_x, min_x) = cin_to_vector<ll>(costs_x);
        cout << min((board_size * min_y) + sum_x, (board_size * min_x) + sum_y) << "\n";
    }
}
