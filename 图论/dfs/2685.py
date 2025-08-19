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
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        parent = [i for i in range(n)]
        cnt = n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            px, py = _min(px, py), _max(px, py)
            parent[py] = px

            nonlocal cnt
            cnt -= 1

        for i in range(n):
            for j in g[i]:
                union(i, j)

        # print(f'cnt: {cnt}')
        # print(f'parent: {parent}')
        # print(f'g: {g}')

        vis = [False] * n

        def judge(u):
            jg = vis[u] = True
            for v in range(n):
                if u == v or find(u) != find(v):
                    continue
                if v not in g[u]:
                    jg = False
                    break
            if not jg:
                for v in range(n):
                    if find(u) == find(v):
                        vis[v] = True
            return jg

        for u in range(n):
            if not vis[u] and not judge(u):
                cnt -= 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.countCompleteComponents(n = 6, edges = [[0, 1], [0, 2], [1, 2], [3, 4]]))
    print(s.countCompleteComponents(n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]))