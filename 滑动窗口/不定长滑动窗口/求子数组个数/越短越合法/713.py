from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    #     if k <= 1:
    #         return 0
        
    #     ans, r, product = 0, 0, 1
    #     for l in range(len(nums)):
    #         while r < len(nums) and product * nums[r] < k:
    #             product *= nums[r]
    #             r += 1
    #         if r > l and product < k:
    #             ans += r - l
    #             # print(f"l: {l}, r: {r}, ans: {ans}, product: {product}")
    #             product //= nums[l]
    #         else:
    #             r = l + 1
    #             product = 1
    #     return ans

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        ans, l, product = 0, 0, 1
        for r in range(len(nums)):
            product *= nums[r]
            while product >= k:
                product //= nums[l]
                l += 1
            ans += r - l + 1
        return ans

# if __name__ == '__main__':
#     s = Solution()
#     print(s.numSubarrayProductLessThanK([57,44,92,28,66,60,37,33,52,38,29,76,8,75,22], 18))