#include <iostream>
#include <vector>
using namespace std;

int seq_sentinel_2d(vector<vector<int>>& A, int x) {
    int n = A.size();

    for (int i = 0; i < n; i++) {
        A[i].push_back(x);

        int j = 0;
        while (A[i][j] != x) j++;

        if (j < (int)A[i].size() - 1) {
            A[i].pop_back();
            return i;
        }

        A[i].pop_back();
    }

    return -1;
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

/*
Contoh Kasus Uji 1:
Input:
Masukkan jumlah baris: 2
Masukkan jumlah kolom: 3
Masukkan elemen matriks:
1 2 3
4 5 6
Masukkan elemen yang dicari: 5
Output:
Elemen ditemukan pada baris ke-1

Contoh Kasus Uji 2:
Input:
Masukkan jumlah baris: 3
Masukkan jumlah kolom: 2
Masukkan elemen matriks:
7 8
9 10
11 12
Masukkan elemen yang dicari: 8
Output:
Elemen ditemukan pada baris ke-0

Contoh Kasus Uji 3:
Input:
Masukkan jumlah baris: 2
Masukkan jumlah kolom: 2
Masukkan elemen matriks:
1 2
3 4
Masukkan elemen yang dicari: 9
Output:
Elemen tidak ditemukan

Contoh Kasus Uji 4:
Input:
Masukkan jumlah baris: 1
Masukkan jumlah kolom: 4
Masukkan elemen matriks:
10 20 30 40
Masukkan elemen yang dicari: 30
Output:
Elemen ditemukan pada baris ke-0

Contoh Kasus Uji 5:
Input:
Masukkan jumlah baris: 3
Masukkan jumlah kolom: 3
Masukkan elemen matriks:
1 1 1
2 2 2
3 3 3
Masukkan elemen yang dicari: 4
Output:
Elemen tidak ditemukan
*/