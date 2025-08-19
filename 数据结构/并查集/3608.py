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


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.part = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        self.part -= 1


class Solution:
    # def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
    #     if not edges:
    #         return 0

    #     def check(t):
    #         uf = UnionFind(n)

    #         for u, v, time in edges:
    #             if time > t:
    #                 uf.merge(u, v)

    #         roots = set()
    #         for i in range(n):
    #             roots.add(uf.find(i))
    #         return len(roots)

    #     left, right = 0, max(edge[2] for edge in edges)
    #     while left <= right:
    #         mid = (left + right) // 2
    #         comp_mid = check(mid)
    #         if comp_mid >= k:
    #             right = mid - 1
    #         else:
    #             left = mid + 1

    #     return left

    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key=lambda x: x[2], reversed=True)

        uf = UnionFind(n)
        for u, v, time in edges:
            uf.merge(u, v)
            if uf.part < k:
                return time

        return 0


if __name__ == "__main__":
    s = Solution()
    print(s.minTime(n=2, edges=[[0, 1, 3]], k=2))
