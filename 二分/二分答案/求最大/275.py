from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, len(citations) - 1
        while l <= r:
            mid = (l + r) // 2
            if n - mid <= citations[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return n - l

# https://leetcode.cn/problems/h-index-ii/description/
solution = Solution()
citations = [0, 1, 3, 5, 6]
print(solution.hIndex(citations))  # Output: 3
citations = [0]
print(solution.hIndex(citations))  # Output: 0