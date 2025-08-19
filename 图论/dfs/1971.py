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
def _max(a, b):
    return a if a > b else b

class ConnectedComponents:
    def __init__(self, n: int, edges: List[List[int]]):
        """初始化图，并计算连通分量"""
        self.n = n
        self.g = [[] for _ in range(n)]
        for u, v in edges:
            self.g[u].append(v)
            self.g[v].append(u)
        
        self.comp_id = [-1] * n  # 节点所属的连通分量ID
        self.comp_sizes = []     # 每个连通分量的大小
        self._calculate_components()
    
    def _calculate_components(self):
        """使用非递归DFS计算连通分量"""
        comp_count = 0
        for i in range(self.n):
            if self.comp_id[i] == -1:  # 未访问节点
                stack = [i]
                comp_size = 0
                self.comp_id[i] = comp_count
                while stack:
                    node = stack.pop()
                    comp_size += 1
                    for neighbor in self.g[node]:
                        if self.comp_id[neighbor] == -1:
                            self.comp_id[neighbor] = comp_count
                            stack.append(neighbor)
                self.comp_sizes.append(comp_size)
                comp_count += 1
        self.comp_count = comp_count
    
    def get_component_count(self) -> int:
        """返回连通分量的总数"""
        return self.comp_count
    
    def get_component_sizes(self) -> List[int]:
        """返回所有连通分量的大小列表"""
        return self.comp_sizes
    
    def get_component_id(self, node: int) -> int:
        """返回指定节点所属的连通分量ID"""
        return self.comp_id[node]
    
    def are_connected(self, u: int, v: int) -> bool:
        """检查两个节点是否连通"""
        return self.comp_id[u] == self.comp_id[v]
    
    def get_components(self) -> List[List[int]]:
        """返回所有连通分量的节点列表（按分量ID排序）"""
        components = [[] for _ in range(self.comp_count)]
        for i in range(self.n):
            components[self.comp_id[i]].append(i)
        return components
    
class UnionFind:
    def __init__(self, n: int) -> None:
        """初始化并查集"""
        self.parent = list(range(n))
        self.rank = [0] * n
        self.part = n

    def find(self, x):
        """查找根节点, 路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
        """合并两个节点所在的集合, 按秩合并"""
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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        cc = ConnectedComponents(n, edges)
        return cc.get_component_id(source) == cc.get_component_id(destination)
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        uf = UnionFind(n)
        for u, v in edges:
            uf.merge(u, v)
        return uf.find(source) == uf.find(destination)
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        
        vis = [False] * n
        def dfs(u):
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
        dfs(source)
        return vis[destination]