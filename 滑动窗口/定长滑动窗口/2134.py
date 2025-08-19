from typing import List
from collections import Counter
# https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        nums = nums + nums
        n = len(nums)
        one_pre_sum = [0] * (n + 1)
        zero_pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            one_pre_sum[i] = one_pre_sum[i - 1] + nums[i - 1]
            zero_pre_sum[i] = zero_pre_sum[i - 1] + (1 - nums[i - 1])
        
        windows_len = one_pre_sum[-1] // 2
        swap__min_cnt = float('inf')
        for l in range(1, n + 1):
            r = l + windows_len - 1
            if r > n:
                break
            zero_num = zero_pre_sum[r] - zero_pre_sum[l - 1]
            swap__min_cnt = min(swap__min_cnt, zero_num)
            
        return swap__min_cnt
            
        

# 测试
if __name__ == '__main__':
    nums = [1, 0, 0, 1, 0, 0, 1, 1]
    print(Solution().minSwaps(nums))