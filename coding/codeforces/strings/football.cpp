#include <cstdio>
#include <iostream>
using namespace std;

main() {
    string s;
    cin >> s;
    int counter = 0;
    char prev = 'a';
    for(char c: s) {
        if(c == prev) {
            counter += 1;
        } else {
            counter = 1;
            prev = c;
        }
        if (counter >= 7) {
            return 0;
        }
    }
    cout << "NO";
}
