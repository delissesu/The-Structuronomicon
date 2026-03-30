#include <bits/stdc++.h>
using namespace std;

class Calculator {
public:
    static int add(int a, int b) {
        return a + b;
    }
    static int subtract(int a, int b) {
        return a - b;
    }
    static int multiply(int a, int b) {
        return a * b;
    }
    static double divide(int a, int b) {
        if (b == 0)
            throw invalid_argument("Dibagi dengan nol");
        return static_cast<double>(a) / b;
    }
};

int main() {
    // Pengujian kasus sederhana
    int a = 20, b = -5;
    cout << "Penjumlahan: " << Calculator::add(a, b) << endl;
    cout << "Pengurangan: " << Calculator::subtract(a, b) << endl;
    cout << "Perkalian: " << Calculator::multiply(a, b) << endl;
    try {
        cout << "Pembagian: " << Calculator::divide(a, b) << endl;
    } catch (const invalid_argument& e) {
        cerr << e.what() << endl;
    }
    return 0;
}