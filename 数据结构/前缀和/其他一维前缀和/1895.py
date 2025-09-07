from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
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

class Solution:
    # 暴力
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_side = min(n, m)
        for side in range(max_side, 0, -1):
            for i in range(n - side + 1):
                for j in range(m - side + 1):
                    if self.isMagicSquare(grid, i, j, side):
                        return side
        return 1

    def isMagicSquare(self, grid: List[List[int]], row: int, col: int, size: int) -> bool:
        target_sum = sum(grid[row][col:col + size])
        for i in range(size):
            if sum(grid[row + i][col:col + size]) != target_sum:
                return False
        for j in range(size):
            if sum(grid[row + i][col + j] for i in range(size)) != target_sum:
                return False
        if sum(grid[row + i][col + i] for i in range(size)) != target_sum:
            return False
        if sum(grid[row + i][col + size - 1 - i] for i in range(size)) != target_sum:
            return False
        return True
    
    # 前缀和
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        max_side = min(n, m)
        
        row_sum = [[0] * (m + 1) for _ in range(n)]
        col_sum = [[0] * (m) for _ in range(n + 1)]
        diag_sum = [[0] * (m + 1) for _ in range(n + 1)]
        anti_diag_sum = [[0] * (m + 2) for _ in range(n + 1)]
        
        for i in range(n):
            for j in range(m):
                row_sum[i][j + 1] = row_sum[i][j] + grid[i][j]
                col_sum[i + 1][j] = col_sum[i][j] + grid[i][j]
                diag_sum[i + 1][j + 1] = diag_sum[i][j] + grid[i][j]
                anti_diag_sum[i + 1][j] = anti_diag_sum[i][j + 1] + grid[i][j]
        
        for side in range(max_side, 0, -1):
            for i in range(n - side + 1):
                for j in range(m - side + 1):
                    target_sum = row_sum[i][j + side] - row_sum[i][j]
                    if all(row_sum[i + k][j + side] - row_sum[i + k][j] == target_sum for k in range(side)) and \
                       all(col_sum[i + side][j + k] - col_sum[i][j + k] == target_sum for k in range(side)) and \
                       diag_sum[i + side][j + side] - diag_sum[i][j] == target_sum and \
                       anti_diag_sum[i + side][j] - anti_diag_sum[i][j + side] == target_sum:
                        return side
        return 1