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
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        pre_cnt = [[0] * 26]
        for c in s:
            pre_cnt.append(pre_cnt[-1].copy())
            pre_cnt[-1][ord(c) - ord('a')] += 1
        
        ans = []
        for l, r, k in queries:
            odd_cnt = 0
            for i in range(26):
                if (pre_cnt[r + 1][i] - pre_cnt[l][i]) % 2 == 1:
                    odd_cnt += 1
            ans.append(odd_cnt // 2 <= k)
        return ans
    
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        pre_cnt = [[0] * 26]
        for c in s:
            pre_cnt.append(pre_cnt[-1].copy())
            pre_cnt[-1][ord(c) - ord('a')] += 1
            pre_cnt[-1][ord(c) - ord('a')] %= 2
            
        ans = []
        for l, r, k in queries:
            odd_cnt = 0
            for i in range(26):
                if pre_cnt[r + 1][i] != pre_cnt[l][i]:
                    odd_cnt += 1
            ans.append(odd_cnt // 2 <= k)
        return ans