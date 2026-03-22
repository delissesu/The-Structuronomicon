#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

bool palindrom(string s) {

    // s.erase(remove(s.begin(), s.end(), ' '), s.end());a
    // string clean;
    // for ( char ch : s ) {
    //     if ( ch != ' ' ) {
    //         clean.push_back(tolower(ch));
    //     }
    // }

    // s = clean;
    
    // for ( char &ch : s ) {
    //     ch = tolower(ch);
    // }

    if (s.size() == 0) {
        return true;
    }
    
    if (s.size() == 1) {
        return true;
    }
    
    char c = s[0];
    int karakter_terakhir = s.size() - 1;
    
    // if (s.size() == 2 && (c == s[karakter_terakhir])) {
    //     return true;
    // }
    
    // if (c == s[karakter_terakhir]) {
    //     karakter_terakhir -= 1;
    //     return palindrom(s.substr(1, karakter_terakhir));
    // } else {
    //     return false;
    // }

    if ( s.size() == 2 ) {
        return c == s[karakter_terakhir];
    }

    if ( c != s[karakter_terakhir]) {
        return false;
    }

    // if (s.size() == 2 && (c != s[karakter_terakhir])) {
    //     return false;
    // } else if (s.size() > 2) {
    //     if (c != s[karakter_terakhir]) {
    //         return false;
    //     } else {
    //         return true;
    //     }
    // }

    return palindrom(s.substr(1, karakter_terakhir - 1));
}

// Fungsi main() di bawah tidak boleh diubah!
int main() {
    cout << palindrom("") << endl;
    cout << palindrom("x") << endl;
    cout << palindrom("aa") << endl;
    cout << palindrom("ab") << endl;
    cout << palindrom("ini") << endl;
    cout << palindrom("itu") << endl;
    cout << palindrom("anna") << endl;
    cout << palindrom("ibu ratna antar ubi") << endl;
    cout << palindrom("rumah murah") << endl;
    cout << palindrom("aku suka rajawali bapak apabila wajar aku suka") << endl;
}
