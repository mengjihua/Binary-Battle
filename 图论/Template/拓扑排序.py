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
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class TOPO:
    def __init__(self, n: int, edges: List[List[int]]):
        # self.n = n
        # self.adj = [[] for _ in range(n)]
        # self.indeg = [0] * n
        self.topo_order = self.topologicalSort(n, edges)

    # def addEdge(self, u, v):
    #     self.adj[u].append(v)
    #     self.indeg[v] += 1

    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        返回有向无环图(DAG)的一个拓扑序。
        如果图中存在环，则返回空列表。
        实现: Kahn 算法(基于入度的拓扑排序)
        :param n: 节点数量，节点编号从 0 到 n-1
        :param edges: 边的列表，每条边表示为 [from, to]
        :return: 拓扑排序的节点列表；若存在环，返回空列表
        """
        g = [[] for _ in range(n)]
        in_degree = [0] * n

        for u, v in edges:
            g[u].append(v)
            in_degree[v] += 1

        q = deque(i for i in range(n) if in_degree[i] == 0)
        topo_order = []

        # Kahn 算法
        while q:
            u = q.popleft()
            topo_order.append(u)

            for v in g[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)

        return topo_order if len(topo_order) == n else []