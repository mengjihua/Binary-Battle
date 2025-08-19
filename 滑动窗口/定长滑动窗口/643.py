from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        
        max_sum = 0
        for l in range(1, n - k + 2):
            sum_k = pre_sum[l + k - 1] - pre_sum[l - 1]
            max_sum = max(sum_k, max_sum)
        
        return max_sum / k
    
if __name__ == '__main__':
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    solution = Solution()
    print(solution.findMaxAverage(nums, k))