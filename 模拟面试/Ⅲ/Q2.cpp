#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int n = nums.size(), ans = 0;
        unordered_map<int, int> dic;
        vector<int> pre(n + 1, 0);
        for (int i = 0; i < n; i++) {
            pre[i + 1] = pre[i] + nums[i];
        }
        for (int s : pre) {
            ans += dic[s - k];
            dic[s] += 1;
        }
        return ans;
    }
};