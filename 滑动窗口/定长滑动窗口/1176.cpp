#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    // int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
    //     int ans = 0;
    //     int n = calories.size();
    //     vector<int> pre_sum(n + 1, 0);

    //     for (int i = 1; i < n + 1; i++){
    //         pre_sum[i] = pre_sum[i - 1] + calories[i - 1];
    //     }

    //     for (int i = 1; i < n - k + 2; i++){
    //         int s = pre_sum[i + k - 1] - pre_sum[i - 1];
    //         if (s < lower) ans -= 1;
    //         else if (s > upper) ans += 1;
    //     }

    //     return ans;
    // }

    
    int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
        int ans = 0;
        int n = calories.size();
        int window_sum = 0;

        for (int i = 0; i < n; i++){
            window_sum += calories[i];
            if (i < k - 1) continue;
            ans += (window_sum > upper ? 1 : (window_sum < lower ? -1 : 0));
            window_sum -= calories[i - k + 1];
        }

        return ans;
    }
};