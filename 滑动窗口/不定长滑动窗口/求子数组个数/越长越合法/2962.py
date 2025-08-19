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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        if nums.count(max_num) < k:
            return 0
        
        ans, r, count = 0, 0, 0
        for l in range(len(nums)):
            while r < len(nums) and count < k:
                if nums[r] == max_num:
                    count += 1
                r += 1
            if count >= k:
                ans += len(nums) - r + 1
            if nums[l] == max_num:
                count -= 1
        return ans

    # def countSubarrays(self, nums: List[int], k: int) -> int:
    #     max_num = max(nums)
    #     if nums.count(max_num) < k:
    #         return 0
        
    #     ans, r, count = 0, 0, 0
    #     window = defaultdict(int)
    #     for l in range(len(nums)):
    #         while r < len(nums) and window[max_num] < k:
    #             window[nums[r]] += 1
    #             r += 1
    #         if window[max_num] >= k:
    #             ans += len(nums) - r + 1
    #         window[nums[l]] -= 1
    #     return ans