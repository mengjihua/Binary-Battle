from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid[0])):
            last_num = -1
            for j in range(len(grid)):
                if last_num < grid[j][i]:
                    last_num = grid[j][i]
                else:
                    ans += last_num - grid[j][i] + 1
                    last_num += 1
        return ans