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

void testSecurity() {
    try {
        // Simulasi uji keamanan
        int a = 10;
        int b = 0;
        cout << Calculator::divide(a, b) << endl;
    } catch (const invalid_argument& e) {
        cerr << "Menangkap pengecualian yang diharapkan: " << e.what() << endl;
    }
}

int main() {
    testSecurity();
    return 0;
}