from typing import List, Tuple, Dict, Set, Optional
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
    # def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     nums.sort()

    #     def check(x):
    #         for i in range(x):
    #             if nums[i] * 2 > nums[i - x]:
    #                 return False
    #         return True
                

    #     l, r = 0, n // 2
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if check(mid):
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     return r * 2

    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        l = 0
        for r in range(ceil(n / 2), n):
            if nums[l] * 2 <= nums[r]:
                l += 1
        return l * 2


if __name__ == '__main__':
    s = Solution()
    print(s.maxNumOfMarkedIndices(nums=[3, 5, 2, 4]))
    print(s.maxNumOfMarkedIndices(nums=[9, 2, 5, 4]))
