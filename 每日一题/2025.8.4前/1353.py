from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys
sys.setrecursionlimit(10 ** 5 + 1)


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.part = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y):
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
    def maxEvents(self, events: List[List[int]]) -> int:
        max_time = max(end for _, end in events)
        
        groups = [[] for _ in range(max_time + 1)]
        for start, end in events:
            groups[start].append(end)
        
        ans = 0
        ends = []
        for i, group in enumerate(groups):
            while ends and ends[0] < i:
                heappop(ends)
            for end in group:
                heappush(ends, end)
            if ends:
                heappop(ends)
                ans += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    # print(solution.maxEvents(events=[[1, 2], [2, 3], [3, 4]]))
    # print(solution.maxEvents(events=[[1, 2], [2, 3], [3, 4], [1, 2]]))
    print(solution.maxEvents([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]))
