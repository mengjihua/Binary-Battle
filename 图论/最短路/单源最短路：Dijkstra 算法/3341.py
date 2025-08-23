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
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        heap = [(0, 0, 0)]
        times = [[inf] * m for _ in range(n)]
        times[0][0] = 0
        while heap:
            cur_time, x, y = heappop(heap)
            if cur_time > times[x][y]:
                continue
            if x == n - 1 and y == m - 1:
                return cur_time
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    new_time = _max(cur_time, moveTime[nx][ny]) + 1
                    if new_time < times[nx][ny]:
                        times[nx][ny] = new_time
                        heappush(heap, (new_time, nx, ny))
        return -1