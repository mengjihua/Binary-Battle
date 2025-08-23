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


class ShortestPath:
    """
    最短路径算法模板类，支持 Dijkstra 和 Floyd 算法。
    节点编号从 1 开始。
    """
    def __init__(self):
        pass
    
    def dijkstra(self, n: int, edges: List[List[int]], start: int, directed: bool = False) -> List[float]:
        g = [[] for _ in range(n + 1)]
        for u, v, w in edges:
            g[u].append((v, w))
            if not directed:
                g[v].append((u, w))

        dis = [inf] * (n + 1)
        dis[start] = 0
        heap = [(0, start)]

        while heap:
            d, u = heappop(heap)
            if d > dis[u]:
                continue
            for v, w in g[u]:
                new_d = dis[u] + w
                if new_d < dis[v]:
                    dis[v] = new_d
                    heappush(heap, (new_d, v))

        return dis

    def floyd(self, n: int, edges: List[List[int]], directed: bool = False) -> List[List[float]]:
        f = [[inf] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            f[i][i] = 0

        for u, v, w in edges:
            f[u][v] = min(f[u][v], w)
            if not directed:
                f[v][u] = min(f[v][u], w)

        for k in range(n + 1):
            for i in range(n + 1):
                if f[i][k] == inf:
                    continue
                for j in range(n + 1):
                    if f[i][k] + f[k][j] < f[i][j]:
                        f[i][j] = f[i][k] + f[k][j]

        return f

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        sp = ShortestPath()
        max_time = max(sp.dijkstra(n, times, k, True)[1:])
        return max_time if max_time < inf else -1