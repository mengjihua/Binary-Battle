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
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Spreadsheet:

    def __init__(self, rows: int):
        self.dic = defaultdict(list)
        for i in range(26):
            self.dic[i] = [0] * rows

    def setCell(self, cell: str, value: int) -> None:
        c = ord(cell[0]) - ord('A')
        i = int(cell[1:]) - 1
        self.dic[c][i] = value

    def resetCell(self, cell: str) -> None:
        c = ord(cell[0]) - ord('A')
        i = int(cell[1:]) - 1
        self.dic[c][i] = 0
        
    def get_cell_value(self, cell: str) -> int:
        if cell[0] in alpha:
            c = ord(cell[0]) - ord('A')
            i = int(cell[1:]) - 1
            return self.dic[c][i]
        else:
            return int(cell)

    def getValue(self, formula: str) -> int:
        cell1, cell2 = formula[1:].split('+')
        return self.get_cell_value(cell1) + self.get_cell_value(cell2)
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)