#include <iostream>
#include <string>
using namespace std;

string biner(int n) {
    if (n == 0) return "0";
    if ( n == 1) return "1";
    
    // if (n % 2 == 0) {
    //     return biner(n / 2);
    // } else {
    //     return biner(n / 2);
    // }
    
    string hasil = biner(n / 2);
    hasil += ( n % 2 == 0 ? "0" : "1");
    
    // string rev_hasil;
    // int phsl = hasil.size();
    
    return hasil;
    
    // for (int i = phsl - 1; i >= 0; i--) {
    //     rev_hasil += hasil[i];
    // }
    
    // return rev_hasil;
}

// Fungsi main() di bawah tidak boleh diubah!
int main() {
    cout << biner(0) << endl;
    cout << biner(1) << endl;
    cout << biner(512) << endl;
    cout << biner(1697) << endl;
    cout << biner(1048575) << endl;
}
