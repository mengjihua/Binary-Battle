from typing import List
from math import ceil
# https://leetcode.cn/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def check(self, x: int, start: List[int], d: int) -> bool:
        temp = start.copy()
        for i in range(len(temp) - 1):
            if temp[i + 1] - temp[i] < x:
                diff = temp[i + 1] - temp[i]
                # print(f"i: {i}, diff: {diff}, d: {d}, temp[i]: {temp[i]}, temp[i + 1]: {temp[i + 1]}")
                if x - diff > d:
                    return False
                temp[i + 1] = temp[i] + x
        return True

    def maxPossibleScore(self, start: List[int], d: int) -> int:
        n = len(start)
        start.sort()
        # print(start)
        l, r = 0, ceil((start[-1] + d - start[0]) / (n - 1))
        # print(f"l: {l}, r: {r}")
        while l <= r:
            mid = (l + r) // 2
            # print(f"l: {l}, r: {r}, mid: {mid}")
            if self.check(mid, start, d):
                l = mid + 1
            else:
                r = mid - 1
        return r

solution = Solution()
start = [6, 0, 3]
d = 2
print(solution.maxPossibleScore(start, d)) # Output: 4
start = [10, 8, 7] # 7 12 18
d = 8
print(solution.maxPossibleScore(start, d)) # Output: 5