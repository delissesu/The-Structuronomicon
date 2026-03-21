#include <iostream>
using namespace std;

int main() {
    int luas[4][3] = {
        {225 * 335, 299 * 278, 300 * 250},
        {215 * 394, 144 * 718, 300 * 290},
        {200 * 400, 240 * 333, 142 * 619},
        {314 * 298, 411 * 198, 333 * 222}
    };

    int harga_jual[3] = {100, 120, 150};

    cout << luas[0] << endl;

    for (int merek = 0; merek <3; merek++) {
            int total = 0;
            for (int toko = 0; toko < 4; toko++) {
                total += luas[toko][merek] * harga_jual[merek];
            }
            
            cout << total << endl;
    } 
}