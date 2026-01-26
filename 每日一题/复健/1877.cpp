#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    int minPairSum(vector<int>& nums) {
        int n = nums.size();
        sort(nums.begin(), nums.end());
        int ans = -INT_MAX;
        for (int i = 0; i < n - 1; i++) {
            ans = max(ans, nums[i] + nums[n - i - 1]);
        }
        return ans;
    }
};