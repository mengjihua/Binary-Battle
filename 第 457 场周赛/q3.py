from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)

# TODO 发题解
class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        if not edges:
            return 0
            
        
        def check(t):
            parent = list(range(n))
            rank = [0] * n
            
            def find_root(x):
                if parent[x] != x:
                    parent[x] = find_root(parent[x])
                return parent[x]
            
            def union(x, y):
                rx, ry = find_root(x), find_root(y)
                if rx == ry:
                    return
                if rank[rx] < rank[ry]:
                    parent[rx] = ry
                elif rank[rx] > rank[ry]:
                    parent[ry] = rx
                else:
                    parent[ry] = rx
                    rank[rx] += 1
            
            for u, v, time_val in edges:
                if time_val > t:
                    union(u, v)
            
            roots = set()
            for i in range(n):
                roots.add(find_root(i))
            return len(roots)
        
        max_time = max(edge[2] for edge in edges)
        left, right = 0, max_time
        while left < right:
            mid = (left + right) // 2
            comp_mid = check(mid)
            if comp_mid >= k:
                right = mid
            else:
                left = mid + 1
                
        return left