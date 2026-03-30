#include <bits\stdc++.h>

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
        if (b == 0) {
            throw invalid_argument("Dibagi dengan nol");
        }
        return static_cast<double>(a) / b;
    }
};

void runTests() {
    // Uji kasus penjumlahan
    assert(Calculator::add(10, 5) == 15);
    assert(Calculator::add(-7, 3) == -4);
    assert(Calculator::add(0, 0) == 0);

    // Uji kasus pengurangan
    assert(Calculator::subtract(20, 5) == 15);
    assert(Calculator::subtract(-5, -10) == 5);
    assert(Calculator::subtract(0, 7) == -7);

    // Uji kasus perkalian
    assert(Calculator::multiply(6, 7) == 42);
    assert(Calculator::multiply(-3, 4) == -12);
    assert(Calculator::multiply(0, 100) == 0);

    // Uji kasus pembagian
    assert(Calculator::divide(25, 5) == 5.0);
    assert(Calculator::divide(-9, 3) == -3.0);
    assert(abs(Calculator::divide(10, 4) - 2.5) < 1e-9);

    // Uji kasus pembagian dengan nol
    try {
        Calculator::divide(5, 0);
        assert(false); // seharusnya tidak sampai sini
    } catch (const invalid_argument& e) {
        assert(true);
    }
}

int main() {
    runTests();
    cout << "Semua tes lulus!" << endl;
    return 0;
}
