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
    # dijkstra
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        
        heap = [(grid[0][0], 0, 0)]
        dis = [[inf] * n for _ in range(n)]
        dis[0][0] = grid[0][0]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while heap:
            d, x, y = heappop(heap)
            if x == n - 1 and y == n - 1:
                return d
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dis[nx][ny] == inf:
                    dis[nx][ny] = fmax(d, grid[nx][ny])
                    heappush(heap, (dis[nx][ny], nx, ny))
        return 0X3F
    
    # bfs + 二分
    # def swimInWater(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
        
    #     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    #     def check(t):
    #         q = deque([(0, 0)])
    #         vis = [[False] * n for _ in range(n)]
    #         vis[0][0] = True
    #         while q:
    #             x, y = q.popleft()
    #             if x == n - 1 and y == n - 1:
    #                 return True
    #             for dx, dy in directions:
    #                 nx, ny = x + dx, y + dy
    #                 if 0 <= nx < n and 0 <= ny < n and not vis[nx][ny] and grid[nx][ny] <= t:
    #                     vis[nx][ny] = True
    #                     q.append((nx, ny))
    #         return False
        
    #     l, r = grid[0][0], n * n
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if check(mid):
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     return l