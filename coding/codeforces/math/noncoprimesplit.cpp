#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"

template <typename T>

void cin_to_vector(vector<T> &vec) {
    for (ll i = 0; i < vec.size(); i++) {
        cin >> vec[i];
    }
}

int smallestDivisor(int n)
{
    if (n % 2 == 0)
        return 2;
 
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0)
            return i;
    }
 
    return n;
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
        ll l, r;
        cin >> l >> r;
        if (r <= 3) {
            cout << -1 << endl;
        } else {
            if (l < r) {
                if (r % 2 != 0) r--;
                cout << 2 << " " << r - 2 << endl;
            } else {
                ll smallest_divisor = smallestDivisor(l);
                if (smallest_divisor == l) {
                    cout << -1 << endl;
                } else {
                    // ggT(r - smallest_divisor, smallest_divisor) = smallest_divisor
                    // this is because ggT(r, smallest_divisor) = smallest_divisor because r = x*smallest_divisor + 0
                    // so (r - smallest_divisor) = (r/smallest_divisor) - (smallest_divisor/smallest_divisor) is an integer
                    // => ggT(r - smallest_divisor, smallest_divisor) = smallest_divisor because r - smallest_divisor = (x-1)*smallest_divisor + 0
                    cout << smallest_divisor << " " << r - smallest_divisor << endl;
                }
            }
        }
    }
}
