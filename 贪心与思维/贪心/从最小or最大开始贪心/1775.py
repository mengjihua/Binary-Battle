from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
    #     sum_nums1, sum_nums2 = sum(nums1), sum(nums2)
    #     if sum_nums1 == sum_nums2:
    #         return 0
    #     if sum_nums1 < sum_nums2:
    #         nums1, nums2 = nums2, nums1
    #         sum_nums1, sum_nums2 = sum_nums2, sum_nums1
        
    #     diff = sum_nums1 - sum_nums2
    #     cnt1, cnt2 = [0] * 7, [0] * 7
    #     for num in nums1:
    #         cnt1[num] += 1
    #     for num in nums2:
    #         cnt2[num] += 1
        
    #     ans = 0
    #     for i in range(1, 7):
    #         if cnt1[6 - i + 1] * (6 - i) + cnt2[i] * (6 - i) >= diff:
    #             return ans + ceil(diff / (6 - i))
    #         else:
    #             ans += cnt1[6 - i + 1] + cnt2[i]
    #             diff -= cnt1[6 - i + 1] * (6 - i) + cnt2[i] * (6 - i)
    #     return -1

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        sum_nums1, sum_nums2 = sum(nums1), sum(nums2)
        if sum_nums1 == sum_nums2:
            return 0
        if sum_nums1 < sum_nums2:
            nums1, nums2 = nums2, nums1
            sum_nums1, sum_nums2 = sum_nums2, sum_nums1
        
        diff = sum_nums1 - sum_nums2
        cnt1, cnt2 = [0] * 7, [0] * 7
        for num in nums1:
            cnt1[num] += 1
        for num in nums2:
            cnt2[num] += 1
        
        ans = 0
        for i in range(1, 7):
            cnt = cnt1[6 - i + 1] + cnt2[i]
            if cnt * (6 - i) >= diff:
                return ans + ceil(diff / (6 - i))
            else:
                ans += cnt
                diff -= cnt * (6 - i)
        return -1