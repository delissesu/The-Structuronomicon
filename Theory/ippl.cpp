#include <bits/stdc++.h>

using namespace std;

void process(int x) {
    if (x > 0) {
        cout << "Positive\n";
    } else if (x < 0) {
        cout << "Negative\n";
    } else {
        cout << "Nol\n";
    }
}

int main() {
    int number;
    cout << "Masukkan Angka: ";
    cin >> number;
    process(number);
    return 0;
}