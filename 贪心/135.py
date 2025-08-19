from typing import List
# https://leetcode.cn/problems/candy/?envType=daily-question&envId=2025-06-02

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        dp = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                dp[i] = dp[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                dp[i] = max(dp[i], dp[i + 1] + 1)
        return sum(dp)

# 测试
if __name__ == '__main__':
    ratings = [1, 0, 2]
    print(Solution().candy(ratings))