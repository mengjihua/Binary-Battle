from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10 ** 5 + 1)
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class UnionFind:
    def __init__(self, n: int) -> None:
        """初始化并查集，包含每个连通块的大小"""
        self.parent = list(range(n))  # 父节点数组
        self.rank = [0] * n           # 秩数组（用于按秩合并）
        self.size = [1] * n           # 每个连通块的大小（初始为1）
        self.part = n                 # 连通块数量（初始为n）

    def find(self, x: int) -> int:
        """查找根节点（带路径压缩）"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x: int, y: int) -> bool:
        """合并两个节点所在的集合（按秩合并）"""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        self.size[rx] += self.size[ry]
        
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        
        self.part -= 1
        return True

    def get_size(self, x: int) -> int:
        """返回节点x所在连通块的大小"""
        return self.size[self.find(x)]

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        uf = UnionFind(n)
        for u, v, score in roads:
            uf.merge(u - 1, v - 1)
            
        root = uf.find(0)
        ans = inf
        for u, _, score in roads:
            if root == uf.find(u - 1):
                ans = _min(ans, score)
        return ans