from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
        cnt_x = defaultdict(int)
        cnt_y = defaultdict(int)
        ans = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    cnt_x[x] += 1
                    cnt_y[y] += 1
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    ans += (cnt_x[x] - 1) * (cnt_y[y] - 1)
        return ans