from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

from sortedcontainers import SortedList

def insort(nums: List[int], x: int):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] < x:
            hi = mid - 1
        else:
            lo = mid + 1
    nums.insert(lo, x)
    

class Solution:    
    def maxXorSubsequences(self, nums: List[int]) -> int:
        # basis = SortedList(key=lambda x: -x)
        basis = []
        for num in nums:
            temp = num
            for b in basis:
                if temp ^ b < temp:
                    temp ^= b
            if temp != 0:
                insort(basis, temp)

        ans = 0
        for b in basis:
            if ans ^ b > ans:
                ans ^= b
        return ans
        
    # def maxXorSubsequences(self, nums: List[int]) -> int:
    #     mx_bit_length = max(nums).bit_length()
    #     basis = [0] * mx_bit_length

    #     def add(x: int) -> None:
    #         for i in range(mx_bit_length - 1, -1, -1):
    #             if (x >> i) & 1:
    #                 if basis[i] == 0:
    #                     basis[i] = x
    #                     return
    #                 else:
    #                     x ^= basis[i]

    #     for num in nums:
    #         add(num)
            
    #     max_xor = 0
    #     for i in range(mx_bit_length - 1, -1, -1):
    #         if basis[i] != 0 and (max_xor >> i) & 1 == 0:
    #             max_xor ^= basis[i]

    #     return max_xor