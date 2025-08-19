def lower_bound(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= target:
            r = mid - 1
        else:
            l = mid + 1
    return l

class Solution(object):
    def countFairPairs1(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        def count(upper):
            res = 0
            j = len(nums) - 1
            for i, x in enumerate(nums):
                while j > i and nums[j] > upper - x:
                    j -= 1
                if j == i:
                    break
                res += j - i
            return res
        return count(upper) - count(lower - 1)
    
    def countFairPairs2(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        nums.sort()
        ans = 0
        for idx, x in enumerate(nums):
            l, r = lower_bound(nums, lower - x, 0, idx), lower_bound(nums, upper - x + 1, 0, idx)
            ans += r - l
        return ans
