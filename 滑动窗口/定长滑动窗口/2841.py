from typing import List
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        
        nums = [0] + nums + [0]
        
        dic = defaultdict(int)
        for i in range(1, k + 1):
            dic[nums[i]] += 1
            
        if len(dic) < m:
            max_sum = 0
        else:
            max_sum = pre_sum[k] - pre_sum[0]
        # print(max_sum)
            
        for l in range(2, n - k + 2):
            sum_k = pre_sum[l + k - 1] - pre_sum[l - 1]
            
            dic[nums[l - 1]] -= 1
            if dic[nums[l - 1]] == 0:
                del dic[nums[l - 1]]
            
            if l + k - 1 <= n:
                dic[nums[l + k - 1]] += 1
            
            # print(f'l: {l}, r: {l + k - 1}, sum_k: {sum_k}, dic: {dic}')
            if sum_k > max_sum and len(dic) >= m:
                max_sum = sum_k
        
        return max_sum

# Example usage:
nums = [1, 1, 1, 3]
m = 2
k = 2
solution = Solution()
print(solution.maxSum(nums, m, k))  # Output: 0