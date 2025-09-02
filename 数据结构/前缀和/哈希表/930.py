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

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        # prefix sum of zeroes i: 以 i 结尾的 连续 0 的个数
        pre_zero_sum = [0] * (n + 1)
        for i in range(n):
            if nums[i] == 0:
                pre_zero_sum[i + 1] = pre_zero_sum[i] + 1
            else:
                pre_zero_sum[i + 1] = 0
        
        ans = l = s = 0
        for r in range(n):
            s += nums[r]
            while l < r and (s > goal or nums[l] == 0):
                s -= nums[l]
                l += 1
            if s == goal:
                ans += pre_zero_sum[l] + 1
        return ans
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        pre = list(accumulate(nums, initial=0))
        ans = 0
        dic = Counter()
        for s in pre:
            ans += dic[s - goal]
            dic[s] += 1
        return ans
