#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int jumlah_baris;
    cin >> jumlah_baris;

    vector<int>output;

    for (int i = 0; i < jumlah_baris; i++) {
        int bil;
        cin >> bil; 

        if (find(output.begin(), output.end(), bil) == output.end()) {
            output.push_back(bil);
        }
    }

    for (int num : output) {
        cout << num << "\n";
    }
    
    return 0;
}