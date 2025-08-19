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

# TODO: 复习BFS
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redg = [[] for _ in range(n)]
        blueg = [[] for _ in range(n)]
        
        for u, v in redEdges:
            redg[u].append(v)
        for u, v in blueEdges:
            blueg[u].append(v)
        
        g = [redg, blueg]
        
        ans = [inf] * n
        ans[0] = 0
        q = deque([(0, 0, 0), (0, 1, 0)]) # (node, color, distance)
        vis = [[False, False] for _ in range(n)]
        while q:
            u, color, d = q.popleft()
            for v in g[color][u]:
                if not vis[v][color]:
                    vis[v][color] = True
                    ans[v] = _min(ans[v], d + 1)
                    q.append((v, 1 - color, d + 1))
        return [d if d < inf else -1 for d in ans]
    
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redg = [[] for _ in range(n)]
        blueg = [[] for _ in range(n)]

        for u, v in redEdges:
            redg[u].append(v)
        for u, v in blueEdges:
            blueg[u].append(v)

        g = [redg, blueg]

        ans = [inf] * n
        ans[0] = 0
        q = deque([(0, 0), (0, 1)]) # (node, color)
        d = 0
        vis = [[False, False] for _ in range(n)]
        while q:
            for _ in range(len(q)):
                u, color = q.popleft()
                if vis[u][color]:
                    continue
                for v in g[color][u]:
                    if not vis[v][color]:
                        vis[v][color] = True
                        ans[v] = _min(ans[v], d + 1)
                        q.append((v, 1 - color))
            d += 1
        return [d if d < inf else -1 for d in ans]