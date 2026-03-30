#include <bits\stdc++.h>

void process(int a, int b) {
    int result;
    if (a > 0 && b > 0) {
        result = a + b; // Penggunaan data: a dan b
    } else {
        result = a - b; // Penggunaan data: a dan b
    }
    std::cout << "Hasil: " << result << std::endl;
}

int main() {
    int num1, num2;
    std::cout << "Masukkan dua angka: ";
    std::cin >> num1 >> num2;
    process(num1, num2);
    return 0;
}