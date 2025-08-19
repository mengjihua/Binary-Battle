from typing import List

class Solution:
#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
# using namespace std;

# int main() {
#     int n, k;
#     cin >> n >> k;
#     vector<long long> prices(n);
#     for (int i = 0; i < n; i++) {
#         cin >> prices[i];
#     }

#     const long long INF = -1e18;
#     vector<vector<vector<long long>>> dp(n+1, vector<vector<long long>>(k+1, vector<long long>(3, INF)));
#     dp[0][0][0] = 0;

#     for (int i = 1; i <= n; i++) {
#         for (int j = 0; j <= k; j++) {
#             // 状态0：无持仓
#             dp[i][j][0] = dp[i-1][j][0];
#             if (j >= 1) {
#                 if (dp[i-1][j-1][1] != INF) {
#                     dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][1] + prices[i-1]);
#                 }
#                 if (dp[i-1][j-1][2] != INF) {
#                     dp[i][j][0] = max(dp[i][j][0], dp[i-1][j-1][2] - prices[i-1]);
#                 }
#             }

#             // 状态1：持有多头
#             long long buy = INF;
#             if (dp[i-1][j][0] != INF) {
#                 buy = dp[i-1][j][0] - prices[i-1];
#             }
#             dp[i][j][1] = max(dp[i-1][j][1], buy);

#             // 状态2：持有空头
#             long long sell = INF;
#             if (dp[i-1][j][0] != INF) {
#                 sell = dp[i-1][j][0] + prices[i-1];
#             }
#             dp[i][j][2] = max(dp[i-1][j][2], sell);
#         }
#     }

#     long long ans = 0;
#     for (int j = 0; j <= k; j++) {
#         ans = max(ans, dp[n][j][0]);
#     }
#     cout << ans << endl;

#     return 0;
# }
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        # 初始化 DP 数组
        dp = [[[float('-inf')] * 3 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 0
        # 遍历每一天
        for i in range(1, n + 1):
            # 遍历每个交易次数
            for j in range(1, k + 1):
                # 状态0：无持仓
                dp[i][j][0] = dp[i - 1][j][0]
                if dp[i - 1][j - 1][1] != float('-inf'):
                    dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][1] + prices[i - 1])
                if dp[i - 1][j - 1][2] != float('-inf'):
                    dp[i][j][0] = max(dp[i][j][0], dp[i - 1][j - 1][2] - prices[i - 1])

                # 状态1：持有多头
                buy = float('-inf')
                if dp[i - 1][j][0] != float('-inf'):
                    buy = dp[i - 1][j][0] - prices[i - 1]
                dp[i][j][1] = max(dp[i - 1][j][1], buy)

                # 状态2：持有空头
                sell = float('-inf')
                if dp[i - 1][j][0] != float('-inf'):
                    sell = dp[i - 1][j][0] + prices[i - 1]
                dp[i][j][2] = max(dp[i - 1][j][2], sell)

        # 找到最大利润
        ans = 0
        for j in range(k + 1):
            ans = max(ans, dp[n][j][0])

        return ans

# 测试
# prices = [2, 4, 1]
# k = 2
# print(maxProfit(k, prices))  # 输出: 2
# prices = [1,7,9,8,2]
# k = 2
# print(maxProfit(k, prices))  # 输出: 14
if __name__ == '__main__':
    prices = [2, 4, 1]
    k = 2
    print(Solution().maximumProfit(prices, k))
    prices = [1,7,9,8,2]
    k = 2
    print(Solution().maximumProfit(prices, k))