#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    char nextGreatestLetter(vector<char>& letters, char target) {
        auto it = upper_bound(letters.begin(), letters.end(), target);
        if (it == letters.end()) return letters[0];
        return *it;
    }
};

// int main() {
//     vector<char> letters = {'c', 'f', 'j'};
//     char target;
//     cin >> target;
//     auto it = upper_bound(letters.begin(), letters.end(), target);
//     cout << (*it) << endl;
//     return 0;
// }