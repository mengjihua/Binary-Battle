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
        
        suf_max = [0] * (n + 1)
        for i in range(n - 1, 1, -1):
            suf_max[i] = fmax(suf_max[i + 1], nums[i])

        ans = 0
        mx, mx_diff = nums[0], 0
        for i in range(1, n - 1):
            mx_diff = fmax(mx_diff, mx - nums[i])
            ans = fmax(ans, mx_diff * suf_max[i + 1])
            mx = fmax(mx, nums[i])
        return ans if ans > 0 else 0
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        suf_max = [0] * (n + 1)
        for i in range(n - 1, 1, -1):
            suf_max[i] = fmax(suf_max[i + 1], nums[i])
        
        ans, mx = 0, nums[0]
        for i in range(1, n - 1):
            ans = fmax(ans, (mx - nums[i]) * suf_max[i + 1])
            mx = fmax(mx, nums[i])
        return ans if ans > 0 else 0
    
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans, mx, mx_diff = 0, fmax(nums[0], nums[1]), nums[0] - nums[1]
        for i in range(2, n):
            ans = fmax(ans, mx_diff * nums[i])
            mx_diff = fmax(mx_diff, mx - nums[i])
            mx = fmax(mx, nums[i])
        return ans if ans > 0 else 0