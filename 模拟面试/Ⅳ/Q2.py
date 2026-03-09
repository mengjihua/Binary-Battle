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


def check(suf_dig, temp, l):
    for j in range(30):
        if not ((not suf_dig[l][j]) or (temp[j] and suf_dig[l][j])):
            return False
    return True
    
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        suf_dig = [[0] * 30 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(30):
                if nums[i] & (1 << j):
                    suf_dig[i][j] = suf_dig[i + 1][j] + 1
                else:
                    suf_dig[i][j] = suf_dig[i + 1][j]
        
        ans = [0] * n
        temp = [0] * 30
        r = -1
            
        for l in range(n):
            if l != 0:
                for j in range(30):
                    if nums[l - 1] & (1 << j):
                        temp[j] -= 1
            
            while not check(suf_dig, temp, l):
                r += 1
                for j in range(30):
                    if nums[r] & (1 << j):
                        temp[j] += 1
            ans[l] = fmax(1, r - l + 1)

        return ans