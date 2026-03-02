#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    int reverseBits(int n) {
        long long res = 0;
        for (int i = 0; i < 32; i++) {
            res += (n & 1) << (31 - i);
            n >>= 1;
        }
        return res;
    }
};