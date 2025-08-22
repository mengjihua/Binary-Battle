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
    def minimumArea(self, grid: List[List[int]]) -> int:
        mn_x, mx_x, mn_y, mx_y = inf, -inf, inf, -inf
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    mx_x = _max(mx_x, i)
                    mn_x = _min(mn_x, i)
                    mx_y = _max(mx_y, j)
                    mn_y = _min(mn_y, j)
        return (mx_x - mn_x + 1) * (mx_y - mn_y + 1)
    
    
    # 每个变量单独求来优化时间
    def minimumArea(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def get1():
            for j in range(m):
                for i in range(n):
                    if grid[i][j] == 1:
                        return j
        def get2():
            for j in range(m - 1, -1, -1):
                for i in range(n):
                    if grid[i][j] == 1:
                        return j
                    
        def get11():
            for i in range(n):
                for j in range(m):
                    if grid[i][j] == 1:
                        return i
        
        def get22():
            for i in range(n - 1, -1, -1):
                for j in range(m):
                    if grid[i][j] == 1:
                        return i
                    
        l, r = get1(), get2()
        hi, lo = get11(), get22()
        
        return (lo - hi + 1) * (r - l + 1)
