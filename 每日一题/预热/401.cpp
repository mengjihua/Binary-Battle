#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    vector<string> readBinaryWatch(int turnedOn) {
        vector<string> ans;
        for (int h = 0; h < 12; ++h) {
            bitset<8> sh(h);
            for (int m = 0; m < 60; ++m) {
                bitset<8> sm(m);
                if (sh.count() + sm.count() == turnedOn) {
                    ans.push_back(to_string(h) + ":" + (m < 10 ? "0" : "") + to_string(m));
                }
            }
        }
        return ans;
    }
};

