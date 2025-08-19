from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        ans = 0
        st = set(nums)
        for x in st:
            if x - 1 in st:
                continue
            
            y = x + 1
            while y in st:
                y += 1
            ans = max(ans, y - x)
        return ans