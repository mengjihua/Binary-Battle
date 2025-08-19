from typing import List

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        l, r = 1, min(max(candies), sum(candies) // k)
        # print(l, r, min(max(candies), sum(candies) // k))
        while l <= r:
            mid = (l + r) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}")
            if sum(candy // mid for candy in candies) >= k:
                l = mid + 1
            else:
                r = mid - 1
        return r


solution = Solution()
print(solution.maximumCandies([5,8,6], 3))
print(solution.maximumCandies([2,5], 11))
print(solution.maximumCandies([1], 1))
print(solution.maximumCandies([1,2,6,8,6,7,3,5,2,5], 3))