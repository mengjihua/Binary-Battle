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