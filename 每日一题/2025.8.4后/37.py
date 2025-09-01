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
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = defaultdict(set)

         # 预处理，记录已经填入的数字
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = board[i][j]
                    row[i].add(num)
                    col[j].add(num)
                    box[(i // 3, j // 3)].add(num)

        def dfs(i, j):
            if i == 9:
                return True
            if j == 9:
                return dfs(i + 1, 0)
            if board[i][j] != '.':
                return dfs(i, j + 1)
            for num in map(str, range(1, 10)):
                if (num not in row[i] and num not in col[j] and num not in box[(i // 3, j // 3)]):
                    board[i][j] = num
                    row[i].add(num)
                    col[j].add(num)
                    box[(i // 3, j // 3)].add(num)
                    if dfs(i, j + 1):
                        return True
                    board[i][j] = '.'
                    row[i].remove(num)
                    col[j].remove(num)
                    box[(i // 3, j // 3)].remove(num)
            return False

        dfs(0, 0)