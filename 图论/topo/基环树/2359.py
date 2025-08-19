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

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        if node1 == node2: return node1
        
        n = len(edges)
        
        def get_dist(node: int) -> List[int]:
            # 可能有环，所以需要判断是否访问过
            dist = [inf] * n
            dist[node] = 0
            vis = [False] * n
            vis[node] = True
            while True:
                nxt = edges[node]
                if nxt == -1 or vis[nxt]: break
                vis[nxt] = True
                dist[nxt] = dist[node] + 1
                node = nxt
            return dist
    
        # 获取两个节点到其他节点的距离
        d1 = get_dist(node1)
        d2 = get_dist(node2)
        
        # 找到两个节点到某个节点的距离的较大值的最小值
        min_max_dist = inf
        ans = -1
        for i in range(n):
            dis = _max(d1[i], d2[i])
            if dis < min_max_dist:
                min_max_dist = dis
                ans = i
        return ans