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
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[i + 1] if i < n - 1 else [] for i in range(n)]
        
        ans = []
        for u, v in queries:
            g[u].append(v)

            dis = [inf] * n
            dis[0] = 0
            q = deque([0])
            while q:
                x = q.popleft()
                for y in g[x]:
                    if dis[y] > dis[x] + 1:
                        dis[y] = dis[x] + 1
                        q.append(y)
            ans.append(dis[n - 1])
        
        return ans
    
    # 优化
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        g = [[i + 1] if i < n - 1 else [] for i in range(n)]

        ans = []
        dis = [inf] * n
        dis[0] = 0
        q = deque([0])
        while q:
            u = q.popleft()
            for v in g[u]:
                if dis[v] > dis[u] + 1:
                    dis[v] = dis[u] + 1
                    q.append(v)
            
        for u, v in queries:
            g[u].append(v)
            
            dis[v] = min(dis[v], dis[u] + 1)
            q = deque([v])
            while q:
                x = q.popleft()
                if x == n - 1:
                    continue
                for y in g[x]:
                    if dis[y] > dis[x] + 1:
                        dis[y] = dis[x] + 1
                        q.append(y)
            ans.append(dis[n - 1])

        return ans