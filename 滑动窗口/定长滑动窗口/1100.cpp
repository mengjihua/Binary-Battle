#include <bits/stdc++.h>
using namespace std;


class Solution {
public:
    int numKLenSubstrNoRepeats(string s, int k) {
        vector<int> cnt(26, 0);
        int n = s.size();
        int ans = 0, dup_cnt = 0;

        for (int i = 0; i < k - 1; i++){
            int c = s[i] - 'a';
            cnt[c] += 1;
            if (cnt[c] > 1) dup_cnt += 1;
        }

        for (int i = k - 1; i < n; i++) {
            int c = s[i] - 'a';
            cnt[c] += 1;

            if (cnt[c] > 1) dup_cnt += 1;
            if (dup_cnt == 0) ans += 1;

            int del_c = s[i - k + 1] - 'a';
            if (cnt[del_c] > 1) dup_cnt -= 1;
            cnt[del_c] -= 1;
        }

        return ans;
    }

    int numKLenSubstrNoRepeats1(string s, int k) {
        vector<int> cnt(26, 0);
        int n = s.size();
        int ans = 0;

        int l = 0, r = 0;
        while (r < n) {
            int c = s[r] - 'a';
            cnt[c] += 1;

            while (cnt[c] > 1) {
                cnt[s[l] - 'a'] -= 1;
                l += 1;
            }

            if (r - l + 1 == k) {
                ans += 1;
                cnt[s[l] - 'a'] -= 1;
                l += 1;
            }
            r += 1;
        }

        return ans;
    }
};