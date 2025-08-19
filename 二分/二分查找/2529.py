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
    def maximumCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg_idx = lower_bound(nums, 0) - 1
        pos_idx = lower_bound(nums, 1)
        neg_len = neg_idx + 1
        pos_len = len(nums) - pos_idx
        return max(neg_len, pos_len)