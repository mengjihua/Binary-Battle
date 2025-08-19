from typing import List
# https://leetcode.cn/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        n = len(nums)
        f = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j - 1], pre_sum[i] - pre_sum[k]))
        
        return f[n][m]