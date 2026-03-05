#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        // int idx = find(nums.begin(), nums.end(), target) - nums.begin();
        // if (idx == nums.size()) return -1;
        // return idx;
        int idx = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
        return idx < nums.size() && nums[idx] == target ? idx : -1;
    }
};