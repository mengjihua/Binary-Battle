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
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        
        xor_mx = 0
        for num in nums:
            xor_mx |= num
        
        ans = 0
        states = 1 << n
        for state in range(1, states):
            temp = 0
            for i in range(n):
                if state & (1 << i):
                    temp |= nums[i]
            if temp == xor_mx:
                ans += 1
        return ans
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for num in nums:
            mx |= num
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def dfs(i, cur):
            if i == n:
                return 1 if cur == mx else 0

            a = dfs(i + 1, cur | nums[i])
            b = dfs(i + 1, cur)
            return a + b

        return dfs(0, 0)
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for num in nums:
            mx |= num
        n = len(nums)
        
        @lru_cache(maxsize=None)
        def dfs(i, cur):
            if cur == mx:
                return 1 << (n - i)
            if i == n:
                return 0
            
            a = dfs(i + 1, cur | nums[i])
            b = dfs(i + 1, cur)
            return a + b
        
        return dfs(0, 0)