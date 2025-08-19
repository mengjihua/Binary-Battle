# https://leetcode.cn/problems/koko-eating-bananas/
from typing import List
import math

class Solution:
    def check(self, x: int, piles: List[int], h: int) -> bool:
        judge = 0
        for pile in piles:
            judge += math.ceil(pile / x)
        return judge <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = sum(piles) // h, max(piles)
        if l == 0: l += 1
        while l <= r:
            mid = (l + r) // 2
            if self.check(mid, piles, h):
                r = mid - 1
            else:
                l = mid + 1
        return l

# Example usage:
solution = Solution()
piles = [3,6,7,11]
h = 8
print(solution.minEatingSpeed(piles, h))  # Output: 4