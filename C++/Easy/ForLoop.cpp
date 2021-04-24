#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int start, stop;
    cin >> start;
    cin >> stop;
    for (int i=start; i<stop+1; i++) {
        if (i > 9) {
            if (i % 2 == 0) {
                cout << "even" << endl;
            } else {
                cout << "odd" << endl;
            }
        } else {
            if (i == 1) {
                cout << "one" << endl;
            } else if (i == 2) {
                cout << "two" << endl;
            } else if (i == 3) {
                cout << "three" << endl;
            } else if (i == 4) {
                cout << "four" << endl;
            } else if (i == 5) {
                cout << "five"<< endl;
            } else if (i == 6) {
                cout << "six" << endl;
            } else if (i == 7) {
                cout << "seven" << endl;
            } else if (i == 8) {
                cout << "eight" << endl;
            } else if (i == 9) {
                cout << "nine" << endl;
            }
        }
    }
}
