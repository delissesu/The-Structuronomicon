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
            throw invalid_argument("Dibagi nol");
        return static_cast<double>(a) / b;
    }
};

void measurePerformance() {
    auto start = chrono::high_resolution_clock::now();

    // Simulasi beban kerja
    for (int i = 0; i < 1000000; ++i) {
        Calculator::add(i, i);
        Calculator::subtract(i, i);
        Calculator::multiply(i, i);
        try {
            Calculator::divide(i, 1);
        } catch (const invalid_argument& e) {
            // Menangani pengecualian
        }
    }

    auto end = chrono::high_resolution_clock::now();
    chrono::duration<double> duration = end - start;
    cout << "Uji kinerja selesai di " << duration.count() << " detik." << endl;
}

int main() {
    measurePerformance();
    return 0;
}
