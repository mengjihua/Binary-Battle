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
MOD = 10 ** 9 + 7

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w * 2))
        
        heap = [(0, 0)]
        dis = [inf] * n
        dis[0] = 0
        while heap:
            d, u = heappop(heap)
            if d > dis[u]: continue
            if u == n - 1: return d
            for v, w in g[u]:
                if d + w < dis[v]:
                    dis[v] = d + w
                    heappush(heap, (dis[v], v))
        return -1            
    
if __name__ == "__main__":
    print(Solution().minCost(n = 4, edges = [[0,1,3],[3,1,1],[2,3,4],[0,2,2]]))