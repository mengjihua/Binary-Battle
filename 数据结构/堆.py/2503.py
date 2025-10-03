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
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        heap = []
        heappush(heap, (grid[0][0], 0, 0))
        
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cnt = 0
        
        mx = max(queries)
        score = [0] * (mx + 1)
        limit = grid[0][0]
        

        while heap:
            val, x, y = heappop(heap)
            if val >= mx:
                break
            
            cnt += 1
            limit = fmax(limit, val)
            score[limit + 1] = cnt
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                    heappush(heap, (grid[nx][ny], nx, ny))
                    vis[nx][ny] = True
                    
        for i in range(1, mx + 1):
            score[i] = fmax(score[i], score[i - 1])
        return [score[q] for q in queries]
    
    # 离线处理 + 最小堆
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        heap = []
        heappush(heap, (grid[0][0], 0, 0))
        
        vis = [[False] * n for _ in range(m)]
        vis[0][0] = True
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        cnt = 0
        
        ans = [0] * len(queries)
        # 查询的下标按照查询值从小到大排序，方便离线处理
        for qi, q in sorted(enumerate(queries), key=lambda p: p[1]):
            while heap and heap[0][0] < q:
                cnt += 1
                _, x, y = heappop(heap)
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                        heappush(heap, (grid[nx][ny], nx, ny))
                        vis[nx][ny] = True
            ans[qi] = cnt
        return ans