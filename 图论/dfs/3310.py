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
sys.setrecursionlimit(2 * 10 ** 5 + 1)
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        vis = [False] * n
        indegree = [0] * n
        g = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)
            indegree[v] += 1
        
        def dfs(u):
            vis[u] = True
            for v in g[u]:
                indegree[v] -= 1
                if not vis[v]:
                    dfs(v)
        dfs(k)
        
        if any(vis[i] and indegree[i] > 0 for i in range(n)):
            return [i for i in range(n)]
        return [i for i in range(n) if not vis[i]]
    
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        vis = [False] * n
        indegree = [0] * n
        g = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)
            indegree[v] += 1
            
        q = deque([k])
        vis[k] = True
        while q:
            u = q.popleft()
            for v in g[u]:
                indegree[v] -= 1
                if not vis[v]:
                    vis[v] = True
                    q.append(v)
        
        if any(vis[i] and indegree[i] > 0 for i in range(n)):
            return [i for i in range(n)]
        return [i for i in range(n) if not vis[i]]
    
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for u, v in invocations:
            g[u].append(v)
        
        q = deque([k])
        vis = [False] * n
        vis[k] = True
        while q:
            u = q.popleft()
            for v in g[u]:
                if not vis[v]:
                    vis[v] = True
                    q.append(v)

        if any(not vis[u] and vis[v] for u, v in invocations):
            return [i for i in range(n)]
        return [i for i in range(n) if not vis[i]]