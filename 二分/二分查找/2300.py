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
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        n, m = len(spells), len(potions)
        pairs = [0] * n
        for i in range(n):
            if success % spells[i] == 0:
                temp = success // spells[i]
            else:
                temp = success // spells[i] + 1
            pairs[i] = m - lower_bound(potions, temp)
        return pairs