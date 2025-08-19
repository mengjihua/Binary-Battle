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
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        pre_sum = [0] * n
        r_bound = [-1] * n
        pre_sum[0] = 1 if s[0] == '*' else 0
        r_bound[0] = 0 if s[0] == '|' else -1
        
        for i in range(1, n):
            if s[i] == '*':
                pre_sum[i] = pre_sum[i - 1] + 1
                r_bound[i] = r_bound[i - 1]
            else:
                pre_sum[i] = pre_sum[i - 1]
                r_bound[i] = i
                
        l_bound = [n] * n
        l_bound[n - 1] = n - 1 if s[n - 1] == '|' else n
        for i in range(n - 2, -1, -1):
            if s[i] == '|':
                l_bound[i] = i
            else:
                l_bound[i] = l_bound[i + 1]
            
        ans = []
        for l, r in queries:
            l, r = l_bound[l], r_bound[r]
            if l > r:
                ans.append(0)
            elif l == 0:
                ans.append(pre_sum[r])
            else:
                ans.append(pre_sum[r] - pre_sum[l - 1])
        return ans