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


class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        pre = [0] * n
        res = 0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    pre[j] += 1
                else:
                    pre[j] = 0
            
            for j in range(n):
                if mat[i][j] == 0:
                    continue
                
                mn = pre[j]
                for k in range(j, -1, -1):
                    if pre[k] == 0:
                        break
                    mn = fmin(mn, pre[k])
                    res += mn
                    
        return res