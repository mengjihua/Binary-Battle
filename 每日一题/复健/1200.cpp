#include <bits/stdc++.h>
using namespace std;
const int MOD = 1e9 + 7;

class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<vector<int>> ans;
        int mn = INT_MAX, n = arr.size();
        for (int i = 0; i < n - 1; i++) {
            int x = arr[i], y = arr[i + 1];
            int diff = y - x;
            if (diff < mn) {
                mn = diff;
                ans.clear();
                ans.push_back({x, y});
            } else if (diff == mn) {
                ans.push_back({x, y});
            }
        }
        return ans;
    }
};