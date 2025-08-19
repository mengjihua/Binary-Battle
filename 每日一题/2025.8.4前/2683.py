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
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        n = len(derived)
        def dfs(i, flag):
            if i == n:
                return flag == 0
            return dfs(i + 1, flag ^ derived[i])
        return dfs(0, 0)
    
    # 非递归
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        flag = True
        for i in derived:
            flag ^= derived[i]
        return flag
    
    # 进一步推导
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # return sum(derived) % 2 == 0
        # return derived.count(1) % 2 == 0
        return not sum(derived) & 1