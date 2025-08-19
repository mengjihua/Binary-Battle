from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # temp = 0
        # for i in range(len(nums)):
        #     temp ^= nums[i]
        # return temp
        l, r = 0, len(nums) // 2 - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[2 * mid] != nums[mid * 2 + 1]:
                r = mid - 1
            else:
                l = mid + 1
        return nums[l * 2]