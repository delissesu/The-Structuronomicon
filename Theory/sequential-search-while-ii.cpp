#include <iostream>
using namespace std;

int seq_sentinel_search(int array[], int n, int key) {
    int *p = array;

    array[n] = key;

    while (*p != key) {
        p++;
    }

    if (p - array < n)
        return p - array;
    else
        return -1;
}

int main() {
    int array[21] = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
                    200, 300, 400, 5006, 110, 550, 440, 330, 331, 41};

    int n = 20;
    int key;

    cout << "Enter value to find: ";
    cin >> key;

    int result = seq_sentinel_search(array, n, key);

    if (result == -1)
        cout << "Number not found" << endl;
    else
        cout << "Found at index " << result << endl;

    return 0;
}

/*
Kasus Uji 1:
Input: 70
Output: Found at index 6

Kasus Uji 2:
Input: 41
Output: Found at index 19

Kasus Uji 3:
Input: 5006
Output: Found at index 13

Kasus Uji 4:
Input: 999
Output: Number not found

Kasus Uji 5:
Input: 10
Output: Found at index 0

Kasus Uji 6:
Input: 331
Output: Found at index 18
*/