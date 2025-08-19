from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        if not online[0] or not online[n - 1]:
            return -1
        
        valid_edges = []
        max_w = 0
        for u, v, w in edges:
            if not (online[u] and online[v]):
                continue
            if v == 0 or u == n - 1:
                continue
            valid_edges.append((u, v, w))
            if w > max_w:
                max_w = w
        
        if not valid_edges:
            return -1
        
        def check(min_w):
            graph = [[] for _ in range(n)]
            for u, v, w in valid_edges:
                if w >= min_w:
                    graph[u].append((v, w))
            
            reachable = [False] * n
            queue = deque([0])
            reachable[0] = True
            while queue:
                u = queue.popleft()
                for v, _ in graph[u]:
                    if not reachable[v]:
                        reachable[v] = True
                        queue.append(v)
            
            if not reachable[n-1]:
                return False
            
            indegree = [0] * n
            for u in range(n):
                if reachable[u]:
                    for v, _ in graph[u]:
                        if reachable[v]:
                            indegree[v] += 1
            
            dist = [inf] * n
            dist[0] = 0
            topo_queue = deque()
            
            for i in range(n):
                if reachable[i] and indegree[i] == 0:
                    topo_queue.append(i)
            
            while topo_queue:
                u = topo_queue.popleft()
                for v, w in graph[u]:
                    if not reachable[v]:
                        continue
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                    indegree[v] -= 1
                    if indegree[v] == 0:
                        topo_queue.append(v)
            
            return dist[n - 1] <= k
        
        l, r = 0, max_w
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.findMaxPathScore(edges = [[0,1,5],[1,3,10],[0,2,3],[2,3,4]], online = [True,True,True,True], k = 10))
    print(s.findMaxPathScore(edges = [[0,1,7],[1,4,5],[0,2,6],[2,3,6],[3,4,2],[2,4,6]], online = [True,True,True,False,True], k = 12))
    print(s.findMaxPathScore(edges = [[2,3,22],[0,2,4],[1,2,42]], online =[True,True,True,True], k =36))
    print(s.findMaxPathScore([[5,6,42],[4,6,75],[1,3,67],[3,4,96],[1,6,45],[0,4,3],[2,4,85],[4,5,2],[3,5,4],[1,2,33],[3,6,33],[2,5,74],[1,5,74]], [True,True,False,True,True,True,True], 48))