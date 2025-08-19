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
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        n = len(watchedVideos)
        
        dis = [inf] * n
        dis[id] = 0
        q = deque([id])
        while q:
            u = q.popleft()
            for v in friends[u]:
                if dis[v] > dis[u] + 1:
                    dis[v] = dis[u] + 1
                    q.append(v)
        
        cnt = defaultdict(int)
        for i in range(n):
            if dis[i] == level:
                for wv in watchedVideos[i]:
                    cnt[wv] += 1
        return sorted(cnt.keys(), key=lambda x: (cnt[x], x))