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
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        vis = [[False] * n for _ in range(m)]
        for j in range(n):
            heappush(heap, (heightMap[0][j], 0, j))
            heappush(heap, (heightMap[m - 1][j], m - 1, j))
            vis[0][j] = vis[m - 1][j] = True
        for i in range(1, m - 1):
            heappush(heap, (heightMap[i][0], i, 0))
            heappush(heap, (heightMap[i][n - 1], i, n - 1))
            vis[i][0] = vis[i][n - 1] = True
        
        ans = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while heap:
            mn_h, x, y = heappop(heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                    if heightMap[nx][ny] < mn_h:
                        ans += mn_h - heightMap[nx][ny]
                    heappush(heap, (max(mn_h, heightMap[nx][ny]), nx, ny))
                    vis[nx][ny] = True
        return ans