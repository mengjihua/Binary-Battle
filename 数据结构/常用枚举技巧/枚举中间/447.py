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
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        def distance_squared(p1: List[int], p2: List[int]) -> int:
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        
        n = len(points)
        ans = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                if i != j:
                    # d = distance_squared(points[i], points[j])
                    # ans += cnt[d] * 2
                    # cnt[d] += 1
                    cnt[distance_squared(points[i], points[j])] += 1
            for c in cnt.values():
                ans += c * (c - 1)
        return ans

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        dis = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                dis[i][j] = dis[j][i] = (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2
        
        ans = 0
        for i in range(n):
            cnt = Counter(dis[i])
            for c in cnt.values():
                ans += c * (c - 1)
        return ans