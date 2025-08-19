import math
import sys
from typing import List

class Solution:
    def check(self, x: int, threshold: int, nums: List[int]) -> bool:
        judge = 0
        for num in nums:
            judge += math.ceil(num / x)
        return judge <= threshold

    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2
            if self.check(mid, threshold, nums):
                r = mid - 1
            else:
                l = mid + 1
        return l

# https://leetcode-cn.com/problems/smallest-divisor-given-threshold/
# 1283. 使结果不超过阈值的最小除数
# 二分答案
# 测试
nums = [1,2,5,9]
threshold = 6
s = Solution()
print(s.smallestDivisor(nums, threshold))