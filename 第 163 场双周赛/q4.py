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
MOD = 10 ** 9 + 7


class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        pos = []
        for i in range(m):
            for j in range(n):
                pos.append((grid[i][j], i, j))
        pos.sort(key=lambda x: x[0])
        
        # vals = [val for val, _, _ in pos]
        
        heap = [(0, 0, 0, 0)]
        dis = [[[inf] * (k + 1) for _ in range(n)] for __ in range(m)]
        dis[0][0][0] = 0

        temp1 = [-1] * (k + 1)
        temp2 = [0] * (k + 1)
        while heap:
            d, i, j, used_k = heappop(heap)
            
            if d > dis[i][j][used_k]: continue
            if i == m - 1 and j == n - 1: return d
            
            for di, dj in [(0, 1), (1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    nd = d + grid[ni][nj]
                    if nd < dis[ni][nj][used_k]:
                        dis[ni][nj][used_k] = nd
                        heappush(heap, (nd, ni, nj, used_k))
            
            if used_k < k and grid[i][j] > temp1[used_k]:
                temp1[used_k] = grid[i][j]
                while temp2[used_k] < len(pos):
                    val, ni, nj = pos[temp2[used_k]]
                    if val > grid[i][j]:
                        break
                    if d < dis[ni][nj][used_k + 1]:
                        dis[ni][nj][used_k + 1] = d
                        heappush(heap, (d, ni, nj, used_k + 1))
                    temp2[used_k] += 1
        
        return -1
    

if __name__ == '__main__':
    s = Solution()
    print(s.minCost(grid = [[3,15],[17,7],[10,8],[23,13],[18,22],[26,18],[21,28],[25,28]], k = 2))