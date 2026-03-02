#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        for (int l = 0; l < n; l++) {
            unordered_set<int> s1, s2;
            for (int r = l; r < n; r++) {
                int num = nums[r];
                if (num & 1) s1.insert(num);
                else s2.insert(num);
                if (s1.size() == s2.size()) ans = max(ans, r - l + 1);
            }
        }
        return ans;
    }
};