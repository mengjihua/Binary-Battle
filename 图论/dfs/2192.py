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
def input(): return stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b


# TODO 逆向求祖先
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)

        vis = [False] * n
        temp = [set() for _ in range(n)]

        def dfs(u):
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
                temp[u].update(temp[v])
                temp[u].add(v)

        for u in range(n):
            if not vis[u]:
                dfs(u)

        ans = [[] for _ in range(n)]
        for u in range(n):
            for v in temp[u]:
                ans[v].append(u)

        return ans

    # 优化
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v].append(u)

        vis = [False] * n
        ans = [set() for _ in range(n)]

        def dfs(u):
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
                ans[u].update(ans[v])
                ans[u].add(v)

        for u in range(n):
            if not vis[u]:
                dfs(u)

        return [sorted(list(ans[i])) for i in range(n)]

    # bfs
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v].append(u)
            
        ans = [set() for _ in range(n)]

        for tu in range(n):
            vis = [False] * n
            q = deque([tu])
            vis[tu] = True
            while q:
                u = q.popleft()
                for v in g[u]:
                    if not vis[v]:
                        vis[v] = True
                        ans[tu].add(v)
                        q.append(v)
                        
        return [sorted(list(ans[i])) for i in range(n)]