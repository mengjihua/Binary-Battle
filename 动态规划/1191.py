from typing import List
# https://leetcode.cn/problems/k-concatenation-maximum-sum/

class Solution:
    # def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
    #     n = len(arr)
    #     dp = [0] * (n * min(2, k) + 1)
    #     for i in range(1, n * min(2, k) + 1):
    #         dp[i] = max(dp[i - 1] + arr[(i - 1) % n], arr[(i - 1) % n])
        
    #     pre_sum = [0] * (n + 1)
    #     for i in range(1, n + 1):
    #         pre_sum[i] = pre_sum[i - 1] + arr[i - 1]
    #     converted_sum = [0] * (n + 1)
    #     for i in range(n - 1, -1, -1):
    #         converted_sum[i] = converted_sum[i + 1] + arr[i]
            
    #     if k == 1:
    #         return max(dp) % (10 **9 + 7)
    #     else:
    #         condition1 = pre_sum[n] * (k - 2) + max(pre_sum) + max(converted_sum)
    #         condition2 = max(dp[1:])
    #         condition3 = 0
    #         print(dp, pre_sum, condition1, condition2, condition3)
    #         return max(condition1, condition2, condition3) % (10**9 + 7)
    
    def maxSubArray(self, nums: List[int]) -> int:
        ans = f = 0  # 本题允许子数组为空，ans 可以初始化成 0
        for x in nums:
            f = max(f, 0) + x
            ans = max(ans, f)
        return ans

    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if k == 1:
            return self.maxSubArray(arr)
        ans = self.maxSubArray(arr + arr)
        ans += max(sum(arr), 0) * (k - 2)
        return ans % 1_000_000_007
    
# 测试
if __name__ == "__main__":
    solution = Solution()
    arr = [-5,-2,0,0,3,9,-2,-5,4]
    k = 5
    print(solution.kConcatenationMaxSum(arr, k)) # 输出: 20