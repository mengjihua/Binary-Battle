from time import time
    
from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)


class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs(u: int, path: List[str]):
            nonlocal ans
            vis[u] = True
            path.append(label[u])

            if ans < len(path) and path == path[::-1]:
                ans = len(path)
                # print(path)

            for v in g[u]:
                if not vis[v]:
                    dfs(v, path)
            vis[u] = False

            path.pop()

        ans = 0
        for i in range(n):
            vis = [False] * n
            dfs(i, [])

        return ans