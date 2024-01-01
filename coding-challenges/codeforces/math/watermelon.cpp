#include <cstdio>
#include <iostream>
using namespace std;

main(int k) {
    cin >> k;
    puts(
        k < 3 || k % 2 ? "NO": "YES"
    );
}
