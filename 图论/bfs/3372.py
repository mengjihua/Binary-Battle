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
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        n, m = len(edges1) + 1, len(edges2) + 1
        
        def build_graph(edges: List[List[int]], size: int) -> List[List[int]]:
            graph = [[] for _ in range(size)]
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)
            return graph

        g1 = build_graph(edges1, n)
        g2 = build_graph(edges2, m)
        
        # 寻找 start 节点到每个距离 <= target_dis 的节点的个数
        def bfs(g: List[List[int]], start: int, target_dis: int, length: int) -> List[int]:
            vis = [False] * length
            vis[start] = True
            q = deque([(start, 0)])
            cnt = 0
            while q:
                cur, dis = q.popleft()
                cnt += 1
                if dis < target_dis:
                    for nxt in g[cur]:
                        if not vis[nxt]:
                            vis[nxt] = True
                            q.append((nxt, dis + 1))
            return cnt
        
        
        base_cnt = []
        for i in range(n):
            base_cnt.append(bfs(g1, i, k, n))
        
        if k == 0:
            return base_cnt
        
        extra_cnt = 0
        for i in range(m):
            extra_cnt = fmax(extra_cnt, bfs(g2, i, k - 1, m))
            
        return [i + extra_cnt for i in base_cnt]
        

# if __name__ == "__main__":
#     s = Solution()
#     print(s.maxTargetNodes(edges1 = [[0,1],[0,2],[2,3],[2,4]], 
#                            edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]], 
#                            k = 2))