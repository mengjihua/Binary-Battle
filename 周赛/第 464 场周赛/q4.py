from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

import bisect
from typing import List

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        rd = sorted(zip(robots, distance))
        sorted_walls = sorted(walls)
        n = len(rd)
        robots_sorted = [r for r, _ in rd]
        left_neighbors = []
        right_neighbors = []
        for i in range(n):
            if i == 0:
                left_neighbors.append(None)
            else:
                left_neighbors.append(robots_sorted[i-1])
            if i == n-1:
                right_neighbors.append(None)
            else:
                right_neighbors.append(robots_sorted[i+1])
        
        def cnt_wall(lo, hi):
            left_idx = bisect.bisect_left(sorted_walls, lo)
            right_idx = bisect.bisect_right(sorted_walls, hi) - 1
            if left_idx > right_idx:
                return 0
            return right_idx - left_idx + 1
        
        intervals = []
        for idx in range(n):
            r, d = rd[idx]
            left_neighbor = left_neighbors[idx]
            right_neighbor = right_neighbors[idx]
            
            if left_neighbor is None:
                L = r - d
            else:
                if left_neighbor < r - d:
                    L = r - d
                else:
                    L = left_neighbor + 1
            
            if right_neighbor is None:
                R = r + d
            else:
                if right_neighbor > r + d:
                    R = r + d
                else:
                    R = right_neighbor - 1
            
            left_count = cnt_wall(L, r)
            right_count = cnt_wall(r, R)
            
            if left_count > right_count:
                intervals.append((L, r))
            else:
                intervals.append((r, R))
        
        if not intervals:
            return 0
        
        intervals.sort()
        merged = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            s, e = intervals[i]
            if s <= end + 1:
                if e > end:
                    end = e
            else:
                merged.append((start, end))
                start, end = s, e
        merged.append((start, end))
        
        total = 0
        for s, e in merged:
            total += cnt_wall(s, e)
        return total
    

if __name__ == "__main__":
    s = Solution()
    robots = [17,59,32,11,72,18]
    distance = [5,7,6,5,2,10]
    walls = [17,25,33,29,54,53,18,35,39,37,20,14,34,13,16,58,22,51,56,27,10,15,12,23,45,43,21,2,42,7,32,40,8,9,1,5,55,30,38,4,3,31,36,41,57,28,11,49,26,19,50,52,6,47,46,44,24,48]
    print(s.maxWalls(robots, distance, walls))