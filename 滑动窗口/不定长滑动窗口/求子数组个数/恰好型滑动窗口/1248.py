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
    # def numberOfSubarrays(self, nums: List[int], k: int) -> int:
    #     ans, l1, l2, odd_cnt1, odd_cnt2 = 0, 0, 0, 0, 0
        
    #     for r, num in enumerate(nums):
    #         odd_cnt1 += num % 2
    #         odd_cnt2 += num % 2

    #         while odd_cnt1 > k:
    #             odd_cnt1 -= nums[l1] % 2
    #             l1 += 1
    #         while l2 <= r and odd_cnt2 >= k:
    #             odd_cnt2 -= nums[l2] % 2
    #             l2 += 1

    #         ans += l2 - l1
            
    #     return ans
    
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def f(k: int) -> int:
            res = l = odd_cnt = 0
            for r, num in enumerate(nums):
                odd_cnt += num % 2
                while l <= r and odd_cnt > k:
                    odd_cnt -= nums[l] % 2
                    l += 1
                res += r - l + 1
            return res
            
        return f(k) - f(k - 1)