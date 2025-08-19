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
    # DFS暴力
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        temp = [set() for _ in range(n)]
        g = [[] for _ in range(n)]
        for u, v in richer:
            g[v].append(u)
            temp[v].add(u)
        
        vis = [False] * n
        def dfs(u):
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
                temp[u].update(temp[v])
            temp[u].add(u)
        
        ans = []
        for i in range(n):
            if not vis[i]:
                dfs(i)
            ans.append(min(temp[i], key=lambda x: quiet[x]))
        return ans
    
    # 记忆化搜索
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        for u, v in richer:
            g[v].append(u)

        @lru_cache(None)
        def dfs(u):
            res = u
            for v in g[u]:
                t = dfs(v)
                if quiet[t] < quiet[res]:
                    res = t
            return res

        return [dfs(i) for i in range(n)]
    
    # TOPO 排序
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = [[] for _ in range(n)]
        in_degree = [0] * n
        for u, v in richer:
            g[u].append(v)
            in_degree[v] += 1

        q = deque(i for i in range(n) if in_degree[i] == 0)
        ans = list(range(n))
        while q:
            u = q.popleft()
            for v in g[u]:
                if quiet[ans[u]] < quiet[ans[v]]:
                    ans[v] = ans[u]
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        return ans
            

if __name__ == "__main__":
    s = Solution()
    print(s.loudAndRich(richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]], quiet = [3,2,5,4,6,1,7,0]))