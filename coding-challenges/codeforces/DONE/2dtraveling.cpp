#include <bits/stdc++.h>
using namespace std;

#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"

main() {
    ios;
    
    #ifndef ONLINE_JUDGE
    freopen(input_file, "r", stdin);
    freopen(output_file, "w", stdout);
    #endif

    ll num_test_cases;
    cin >> num_test_cases;
    while(num_test_cases--) {
        ll n, k, a, b, direct_costs, a_nearest_capital_costs = LLONG_MAX / 2, b_nearest_capital_costs = LLONG_MAX / 2, a_costs_to_capital, b_costs_to_capital;
        cin >> n >> k >> a >> b;
        vector<ll> coordsx(n+1), coordsy(n+1);
        for (ll i = 1; i <= n; i++) {
            cin >> coordsx[i] >> coordsy[i];
        }
        direct_costs = abs(coordsx[a] - coordsx[b]) + abs(coordsy[a] - coordsy[b]);
        for (ll i = 1; i <= k; i++) {
            a_nearest_capital_costs = min(a_nearest_capital_costs, abs(coordsx[a] - coordsx[i]) + abs(coordsy[a] - coordsy[i]));
            b_nearest_capital_costs = min(b_nearest_capital_costs, abs(coordsx[b] - coordsx[i]) + abs(coordsy[b] - coordsy[i]));
        }
        cout << min(direct_costs, a_nearest_capital_costs + b_nearest_capital_costs) << endl;
    }
}
