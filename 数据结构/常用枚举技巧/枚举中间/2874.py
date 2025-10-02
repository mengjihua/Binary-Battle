from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        suf_max = [0] * n
        suf_max[-1] = nums[-1]
        for i in range(n - 2, 1, -1):
            suf_max[i] = fmax(suf_max[i + 1], nums[i])
        
        ans, pre_max = 0, nums[0]
        for i in range(1, n - 1):
            ans = fmax(ans, (pre_max - nums[i]) * suf_max[i + 1])
            pre_max = fmax(pre_max, nums[i])
        return ans
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_num = fmax(nums[0], nums[1])
        diff_max = nums[0] - nums[1]
        ans = 0
        for i in range(2, len(nums)):
            ans = fmax(ans, diff_max * nums[i])
            diff_max = fmax(diff_max, max_num - nums[i])
            max_num = fmax(max_num, nums[i])
        return ans