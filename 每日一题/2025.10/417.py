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
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        pacific_reachable = set()
        atlantic_reachable = set()
        for i in range(m):
            pacific_reachable.add((i, 0))
            atlantic_reachable.add((i, n - 1))
        for j in range(n):
            pacific_reachable.add((0, j))
            atlantic_reachable.add((m - 1, j))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(x: int, y: int, reachable: Set[Tuple[int, int]]):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in reachable:
                        reachable.add((nx, ny))
                        dfs(nx, ny, reachable)
        
        # for i, j in pacific_reachable: ❌
        # -> dfs中pacific_reachable会动态变化, 集合在迭代过程(for)中被修改，从而抛出 RuntimeError
        for i, j in list(pacific_reachable):
            dfs(i, j, pacific_reachable)
        for i, j in list(atlantic_reachable):
            dfs(i, j, atlantic_reachable)
            
        return list(pacific_reachable & atlantic_reachable)
    
    # bfs
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        pacific_reachable = set()
        atlantic_reachable = set()
        for i in range(m):
            pacific_reachable.add((i, 0))
            atlantic_reachable.add((i, n - 1))
        for j in range(n):
            pacific_reachable.add((0, j))
            atlantic_reachable.add((m - 1, j))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def bfs(reachable: Set[Tuple[int, int]]):
            q = deque(reachable)
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y] and (nx, ny) not in reachable:
                        reachable.add((nx, ny))
                        q.append((nx, ny))
        
        bfs(pacific_reachable)
        bfs(atlantic_reachable)
            
        return list(pacific_reachable & atlantic_reachable)