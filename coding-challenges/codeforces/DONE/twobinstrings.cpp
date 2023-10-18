#include <cstdio>
#include <iostream>
using namespace std;

int main() {
    int t;
    string s1, s2;
    cin >> t;
    for (int counter = 0; counter < t; counter++) {
        cin >> s1 >> s2;
        bool same = false;
        int chars = s1.size();
        for (int i = 0; i < chars; i++) {
            if (s1[i] == '0' && s2[i] == '0' && s1[i+1] == '1' && s2[i+1] == '1') {
                same = true;
            }
        }
        if (same) {
            cout << "YES" << "\n";
        } else {
            cout << "NO" << "\n";
        }
    }
}
