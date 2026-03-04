#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        bool desc = true;
        int n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] < nums[i + 1]) {
                desc = false;
                break;
            }
        }
        if (desc) {
            reverse(nums.begin(), nums.end());
            return;
        }

        for (int i = n - 2; i > -1; i--) {
            for (int j = n - 1; j > i; j--) {
                if (nums[i] < nums[j]) {
                    // 不可以用 nums[i], nums[j] = nums[j], nums[i];
                    swap(nums[i], nums[j]);
                    sort(nums.begin() + i + 1, nums.end());
                    return;
                }
            }
        }
    }
};