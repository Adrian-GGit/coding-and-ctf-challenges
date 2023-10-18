#include <cstdio>
#include <iostream>
#include <bits/stdc++.h>
#include <string>
using namespace std;

#define ios ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define ll long long
#define input_file "input.txt"
#define output_file "output.txt"

void solve()
{
    int m;
    string s, l, r;
    cin >> s >> m >> l >> r;        
    int start=-1;
    for (int i = 0; i < m; i++){
        int range=start+1;
        for(char c=l[i];c<=r[i];c++){
            int ind=s.find(c,range);
            if(ind==-1){
                cout<<"YES"<<endl;
                return;
            }
            start=max(ind,start);
        }
    }
 
    cout<<"NO"<<endl;
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
