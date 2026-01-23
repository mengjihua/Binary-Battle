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
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while True:
            n = len(nums)
            judge = True
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    judge = False
                    break
            if judge: break
            
            mn = inf
            idx = -1
            for i in range(n - 1):
                if mn > nums[i] + nums[i + 1]:
                    mn = nums[i] + nums[i + 1]
                    idx = i
                    
            nums[idx] = nums[idx] + nums[idx + 1]
            nums.pop(idx + 1)
            ans += 1
        return ans
            