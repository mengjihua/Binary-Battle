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
def _max(a, b):
    return a if a > b else b

# TODO https://leetcode.cn/problems/number-of-provinces/solutions/3731895/cc-template-jing-tai-dfs-dong-tai-bing-c-oup7
class ConnectedComponents:
    def __init__(self, n: int, edges: List[List[int]]):
        """初始化图，并计算连通分量"""
        self.n = n
        self.g = [[] for _ in range(n)]
        for x, y in edges:
            self.g[x].append(y)
            self.g[y].append(x)
        
        self.vis = [False] * n
        self._calculate_components()
    
    def _dfs(self, x: int) -> int:
        """使用深度优先搜索计算从节点 x 出发的连通块大小"""
        self.vis[x] = True
        size = 1
        for y in self.g[x]:
            if not self.vis[y]:
                size += self._dfs(y)
        return size
    
    def _calculate_components(self):
        """计算所有连通块的大小"""
        self.components_size = []
        for i in range(self.n):
            if not self.vis[i]:
                size = self._dfs(i)
                self.components_size.append(size)
    
    def get_component_sizes(self) -> List[int]:
        """返回所有连通块的大小"""
        return self.components_size
    

class ConnectedComponents2:
    def __init__(self, n: int, edges: List[List[int]]):
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        edges = []
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    edges.append([i, j])
        cc = ConnectedComponents(len(isConnected), edges)
        return len(cc.get_component_sizes())
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        cc2 = ConnectedComponents2(len(isConnected), [[i, j] for i in range(len(isConnected)) for j in range(i + 1, len(isConnected)) if isConnected[i][j] == 1])
        return cc2.get_component_count()
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(i + 1, len(isConnected)):
                if isConnected[i][j] == 1:
                    uf.merge(i, j)
        return uf.part