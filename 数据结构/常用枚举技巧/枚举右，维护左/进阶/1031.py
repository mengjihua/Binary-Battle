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
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        pre = list(accumulate(nums, initial=0))
        ans = 0
        for i in range(n - firstLen + 1):
            fsum = pre[i + firstLen] - pre[i]
            mx_xm = 0
            for j in range(n - secondLen + 1):
                if j + secondLen <= i or j >= i + firstLen:
                    sm = pre[j + secondLen] - pre[j]
                    mx_xm = max(mx_xm, sm)
            ans = max(ans, fsum + mx_xm)
        return ans
    
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        n = len(nums)
        
        pre = list(accumulate(nums, initial=0))
        
        suf_sl_sm = [0] * (n - secondLen + 2)
        for i in range(n - secondLen, -1, -1):
            suf_sl_sm[i] = max(suf_sl_sm[i + 1], pre[i + secondLen] - pre[i])
            
        ans = pre_sm = 0
        for i in range(n - firstLen + 1):
            fl_sm = pre[i + firstLen] - pre[i]
            suf_mx = 0
            if i + firstLen <= n - secondLen:
                suf_mx = suf_sl_sm[i + firstLen]
            if i >= secondLen:
                pre_sm = fmax(pre_sm, pre[i] - pre[i - secondLen])
            ans = fmax(ans, fl_sm + fmax(pre_sm, suf_mx))
        return ans
