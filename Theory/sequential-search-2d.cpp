#include <iostream>
#include <vector>
using namespace std;

int seq_sentinel_2d(vector<vector<int>> A, int x) {
    int n = A.size();

    A.push_back({x});

    int i = 0;
    while (true) {
        int m = A[i].size();
        for (int j = 0; j < m; j++) {
            if (A[i][j] == x) {
                if (i < n)
                    return i;   
                else
                    return -1; 
            }
        }
        i++;
    }
}

int main() {
    int row, col, x;
    cout << "Masukkan jumlah baris: ";
    cin >> row;
    cout << "Masukkan jumlah kolom: ";
    cin >> col;

    vector<vector<int>> A(row, vector<int>(col));
    cout << "Masukkan elemen matriks:\n";
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            cin >> A[i][j];
        }
    }

    cout << "Masukkan elemen yang dicari: ";
    cin >> x;

    int result = seq_sentinel_2d(A, x);
    if (result != -1)
        cout << "Elemen ditemukan pada baris ke-" << result << endl;
    else
        cout << "Elemen tidak ditemukan\n";

    return 0;
}