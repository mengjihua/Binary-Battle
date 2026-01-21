from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, pairwise
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, comb, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7


class Solution:
    # def minBitwiseArray(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     ans = [-1] * len(nums)
    #     for i in range(n):
    #         for j in range(31):
    #             if (nums[i] >> j) & 1:
    #                 ans[i] = nums[i] ^ (1 << j)
    #             else:
    #                 break
    #     return ans

    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        for i, num in enumerate(nums):
            if num == 2:
                nums[i] = -1
            else:
                t = ~num
                nums[i] ^= (t & -t) >> 1
        return nums