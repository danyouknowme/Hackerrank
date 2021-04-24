#include <iostream>
#include <string>
using namespace std;

int main() {
	// Complete the program
    string a, b;
    cin >> a >> b;
    int len_a = a.size(), len_b = b.size();
    string a_plus_b = a+b;
    swap(a[0], b[0]);
    cout << len_a << " " << len_b << endl;
    cout << a_plus_b << endl;
    cout << a << " " << b;
    
  
    return 0;
}
