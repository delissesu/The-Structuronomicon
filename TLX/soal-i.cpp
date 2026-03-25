#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> data;

    for (int i = 0; i < N; i++) {
        int x;
        cin >> x;
        data.push_back(x);
    }

    int n_tl = 0;

    for (int c : data) n_tl += c;
    
    for (int j = 1; j <= data.size(); j++) {
        cout << n_tl - data[j - 1] << endl;
    }
}