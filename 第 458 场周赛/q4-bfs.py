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
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        vis = [[[False] * (1 << n) for _ in range(n)] for _ in range(n)]
        queue = deque()
        ans = 1
        
        for x in range(n):
            mask = 1 << x
            if not vis[x][x][mask]:
                vis[x][x][mask] = True
                queue.append((x, x, mask))
        
        for u, v in edges:
            if label[u] == label[v]:
                mask = (1 << u) | (1 << v)
                tu, tv = min(u, v), max(u, v)
                if not vis[tu][tv][mask]:
                    vis[tu][tv][mask] = True
                    queue.append((tu, tv, mask))
                    ans = 2
        
        while queue:
            x, y, mask = queue.popleft()
            cnt = bin(mask).count('1')
            ans = max(ans, cnt)
            
            for u in g[x]:
                if mask & (1 << u):
                    continue
                for v in g[y]:
                    if u == v or mask & (1 << v) or label[u] != label[v]:
                        continue
                    new_mask = mask | (1 << u) | (1 << v)
                    tu, tv = min(u, v), max(u, v)
                    if not vis[tu][tv][new_mask]:
                        vis[tu][tv][new_mask] = True
                        queue.append((tu, tv, new_mask))
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxLen(n=3, edges=[[0, 1], [1, 2]], label="aba"))
    print(s.maxLen(n=3, edges=[[0, 1], [0, 2]], label="abc"))
    print(s.maxLen(n=4, edges=[[0, 2], [0, 3], [3, 1]], label="bbac"))
    print(s.maxLen(n=5, edges=[[0, 1], [4, 0], [1, 2], [2, 0], [4, 1], [3, 0], [4, 2], [3, 1]], label="stppt"))
