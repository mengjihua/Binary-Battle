#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = 0, ans = 0;
        while (true) {
            int n = nums.size();

            bool judge = true;
            for (int i = 0; i < n - 1; i++) {
                if (nums[i] > nums[i + 1]) {
                    judge = false;
                    break;
                }
            }
            if (judge) break;

            int mn = INT_MAX;
            int idx = -1;
            for (int i = 0; i < n - 1; i++) {
                if (mn > nums[i] + nums[i + 1]) {
                    mn = nums[i] + nums[i + 1];
                    idx = i;
                }
            }
            nums.erase(nums.begin() + idx + 1);
            ans += 1;
        }
        return ans;
    }
};