from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(2 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = cnt = 0
        for num in nums:
            if num == mx:
                cnt += 1
            else:
                cnt = 0
            ans = _max(cnt, ans)
        return ans
    
    def longestSubarray(self, nums: List[int]) -> int:
        ans = cnt = mx = 0
        for num in nums:
            if num == mx:
                cnt += 1
                ans = _max(ans, cnt)
            elif num > mx:
                mx = num
                cnt = ans = 1
            else:
                cnt = 0
        return ans