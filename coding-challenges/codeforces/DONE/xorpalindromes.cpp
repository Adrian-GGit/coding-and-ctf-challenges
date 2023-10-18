#include <iostream>
#include <algorithm>
using namespace std;

#define ll long long

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    ll test_cases;
    cin >> test_cases;
    while (test_cases--) {
        ll n, min_needed = 0, extra = 0;
        string s, t;
        cin >> n >> s;
        t = string(n + 1, '0');
        for (ll i = 0; i < n / 2; i++) {
            if (s[i] == s[n - i - 1]) extra += 2;
            else min_needed += 1;
        }
        for (ll i = min_needed; i <= min_needed + extra; i += 2) {
            t[i] = '1';
            if (s.length() % 2 == 1) t[i+1] = '1';
        }
        cout << t << endl;
    }
    return 0;
}