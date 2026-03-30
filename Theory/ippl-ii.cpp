#include <bits/stdc++.h>

using namespace std;

void classifyNumber(int num) {
    if (num > 0) {
        cout << "Positive" << endl;
    } else if (num < 0) {
        cout << "Negative" << endl;
    } else {
        cout << "Nol" << endl;
    }
}

int main() {
    int number;
    cout << "Masukkan Angka: ";
    cin >> number;
    classifyNumber(number);
    return 0;
}