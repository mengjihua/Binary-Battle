#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    int longestBalanced(string s) {
        int n = s.size();
        int ans = 0;
        for (int l = 0; l < n; l++) {
            vector<int> c_cnt(26, 0);
            int mx = 0, cnt = 0;
            for (int r = l; r < n; r++) {
                int c_ord = s[r] - 'a';
                if (c_cnt[c_ord] == 0) cnt += 1;
                c_cnt[c_ord] += 1;
                mx = max(mx, c_cnt[c_ord]);
                if (mx * cnt == r - l + 1) ans = max(ans, r - l + 1);
            }
        }
        return ans;
    }
};