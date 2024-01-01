#include <iostream>
#include <numeric>
using namespace std;

#define ll long long

ll gcd(ll a, ll b)
{
  if (b == 0)
    return a;
  return gcd(b, a % b);
}
 
ll lcm(ll a, ll b)
{
    return (a / gcd(a, b)) * b;
}

int main() {
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    ll test_cases;
    cin >> test_cases;
    ll n, x, y, max_score, num_dividers_x, num_dividers_y, num_dividers_x_y, range_x, range_y;
    while (test_cases--) {
        max_score = 0;
        cin >> n >> x >> y;
        num_dividers_x = n / x;
        num_dividers_y = n / y;

        num_dividers_x_y = n / lcm(x, y);
        range_x = n - num_dividers_x + num_dividers_x_y;
        max_score += ((n * (n + 1)) / 2) - ((range_x * (range_x + 1)) / 2);
        range_y = num_dividers_y - num_dividers_x_y;
        max_score -= (range_y * (range_y + 1)) / 2;
        cout << max_score << endl;
    }
    return 0;
}