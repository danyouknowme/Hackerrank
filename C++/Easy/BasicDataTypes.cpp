#include <iostream>
#include <cstdio>
#include <iomanip>
using namespace std;

int main() {
    int n1;
    long n2;
    char n3;
    float n4;
    double n5;
    cin >> n1 >> n2 >> n3 >> n4 >> n5;
    cout << n1 << endl;
    cout << n2 << endl;
    cout << n3 << endl;
    cout << fixed << setprecision(3) << n4 << endl;
    cout << fixed << setprecision(9) << n5;
    return 0;
}
