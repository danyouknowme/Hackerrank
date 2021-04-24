#include <iostream>
using namespace std;

void update(int *a, int *b) {
    int sum = *a + *b;
    int diff;
    if (*a - *b >= 0) {
        diff = *a - *b;
    } else {
        diff = -(*a - *b);
    }
    *a = sum;
    *b = diff;
}


int main() {
    int a, b;
    int *pa = &a,*pb = &b;
    cin >> a >> b;
    update(pa, pb);
    cout << a << endl;
    cout << b;
    
    return 0;
}
