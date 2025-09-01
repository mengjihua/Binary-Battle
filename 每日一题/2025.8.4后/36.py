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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 判断每行是否有重复数字
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
        # 判断每列是否有重复数字
        for i in range(9):
            col = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
        # 判断每个3x3子盒子是否有重复数字
        for i in range(3):
            for j in range(3):
                box = set()
                for p in range(3):
                    for q in range(3):
                        if board[i * 3 + p][j * 3 + q] != '.':
                            if board[i * 3 + p][j * 3 + q] in box:
                                return False
                            box.add(board[i * 3 + p][j * 3 + q])
        return True