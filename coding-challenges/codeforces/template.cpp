#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
using namespace std;

#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"

bool revsort(ll a, ll b){return (a > b);}
void reverseStr(string&str){int n=str.length();for(int i=0;i<n/2;i++){swap(str[i],str[n-i-1]);}}
bool ispal(string x){int n=x.size();for(int i=0;i<n/2;i++){if(x[i]!=x[n-i-1])return 0;}return 1;}
int modadd(int a, int b,int m){a%=m;b%=m;return (a+b)%m;}
int modmul(int a, int b,int m){a%=m;b%=m;return (a*b)%m;}
int modsub(int a, int b,int m){a%=m;b%=m;return (a-b)%m;}
int gcd(int a, int b){if(b==0)return a;return gcd(b,a%b);}
int expo(int a, int n,int m){int res=1;while(n){if(n&1){res=modmul(res,a,m);--n;}else{a=modmul(a,a,m);n>>=1;}}return res;}
int expo(int a, int n){int res=1;while(n){if(n&1){res=res*a;--n;}else{a=a*a;n>>=1;}}return res;}

void solve() {
    
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
        solve();
        cout << endl;
    }
}
