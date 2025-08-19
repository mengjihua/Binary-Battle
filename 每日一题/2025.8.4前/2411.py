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
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        cnt = [0] * 30
        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    cnt[i] += 1

        ans = [0] * n
        r = n - 1
        while r > 0:
            judge = True
            for i in range(30):
                bi = nums[r] & (1 << i)
                if bi and cnt[i] == 1:
                    judge = False
                    break
                
        
        
        for i in range(n):
            pass