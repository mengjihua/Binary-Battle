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

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        # 左下角三角形, 包括中间对角线
        # 遍历每个对角线, 进行非递增顺序处理
        for i in range(n):
            diagonal = []
            for j in range(n - i):
                diagonal.append(grid[i + j][j])
            diagonal.sort(reverse=True)
            # print(diagonal)
            for j in range(n - i):
                grid[i + j][j] = diagonal[j]
        # 右上角三角形, 不包括中间对角线
        # 遍历每个对角线, 进行非递增顺序处理
        for i in range(1, m):
            diagonal = []
            for j in range(m - i):
                diagonal.append(grid[j][i + j])
            diagonal.sort()
            # print(diagonal)
            for j in range(m - i):
                grid[j][i + j] = diagonal[j]
        
        return grid
    
# 网格图可视化
def visualize_grid(grid):
    for row in grid:
        print(" ".join(str(x) for x in row))
    print()

if __name__ == '__main__':
    s = Solution()
    grid = [[1,7,3],[9,8,2],[4,5,6]]
    visualize_grid(grid)
    visualize_grid(s.sortMatrix(grid))