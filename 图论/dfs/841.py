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


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        vis = [False] * n
        def dfs(u):
            vis[u] = True
            for key in rooms[u]:
                if not vis[key]:
                    dfs(key)
        dfs(0)
        return all(vis)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]
        vis = [False] * len(rooms)
        vis[0] = True
        while stack:
            u = stack.pop()
            for key in rooms[u]:
                if not vis[key]:
                    vis[key] = True
                    stack.append(key)
        return all(vis)