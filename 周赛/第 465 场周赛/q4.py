from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
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
    def totalBeauty(self, nums: List[int]) -> int:
        n = len(nums)
        dp = defaultdict(int)
        
        for i in range(n):
            x = nums[i]
            temp = defaultdict(int)
            temp[x] += 1
            
            for j in range(i):
                if nums[i] < nums[j]:
                    for g, cnt in dp.items():
                        _gcd = gcd(g, x)
                        temp[_gcd] += cnt
                    
                    for g, cnt in temp.items():
                        dp[g] += cnt
        
        ans = 0
        for g, cnt in dp.items():
            ans = (ans + g * cnt) % MOD
        
        return ans