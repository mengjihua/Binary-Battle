#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        int m = s.size(), n = p.size();
        vector<int> ans;

        unordered_map<char, int> p_cnt;
        for (auto c : p) p_cnt[c]++;

        unordered_map<char, int> cnt;
        for (int i = 0; i < m; i++) {
            cnt[s[i]] += 1;
            
            if (i < n - 1) continue;
            if (cnt == p_cnt) ans.push_back(i - n + 1);

            cnt[s[i - n + 1]] -= 1;
            if (cnt[s[i - n + 1]] == 0) cnt.erase(s[i - n + 1]);
        }

        return ans;
    }
};