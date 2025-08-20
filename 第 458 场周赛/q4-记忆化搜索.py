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

# TODO: 反复学习
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        @lru_cache(maxsize=None)
        def dfs(x, y, mask):
            res = 0
            for u in g[x]:
                if mask & (1 << u):
                    # print(u, (mask & 1 << u))
                    continue
                for v in g[y]:
                    if u == v or mask & (1 << v) or label[u] != label[v]:
                        # print(u < v, u == v, (mask & 1 << v), label[u], label[v])
                        continue
                    tu, tv = min(u, v), max(u, v)
                    # print(x, y, u, v)
                    # print(label[x], label[y], label[u], label[v])
                    # print('-' * 10)
                    res = max(res, dfs(tu, tv, mask | (1 << u) | (1 << v)) + 2)
            return res

        ans = 0
        for x in range(n):
            # 奇回文串
            ans = max(ans, dfs(x, x, 1 << x) + 1)
            if ans == n:
                return n
            # 偶回文串
            for y in g[x]:
                if x > y or label[x] != label[y]:
                    continue
                ans = max(ans, dfs(x, y, (1 << x) | (1 << y)) + 2)
                if ans == n:
                    return ans
        return ans
    

if __name__ == "__main__":
    s = Solution()
    # print(s.maxLen(n = 3, edges = [[0,1],[1,2]], label = "aba"))
    # print(s.maxLen(n = 3, edges = [[0,1],[0,2]], label = "abc"))
    # print(s.maxLen(n = 5, edges = [[0,1],[4,0],[1,2],[2,0],[4,1],[3,0],[4,2],[3,1]], label = "stppt"))
    print(s.maxLen(n=7,edges=[[0,1],[1,2],[1,3],[3,4],[0,5],[5,6]],label="aabbcbc"))