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

class SegmentTree:
    def __init__(self, lst: List[int]):
        n = len(lst)
        self.max = [0] * (2 << (n - 1).bit_length())
        self.build(lst, 0, 0, n - 1)
        
    def maintain(self, i: int):
        self.max[i] = _max(self.max[i * 2 + 1], self.max[i * 2 + 2])
    
    def build(self, lst: List[int], i: int, l: int, r: int):
        if l == r:
            self.max[i] = lst[l]
            return
        mid = (l + r) // 2
        self.build(lst, i * 2 + 1, l, mid)
        self.build(lst, i * 2 + 2, mid + 1, r)
        self.maintain(i)
        
    # 找到区间的第一个 >= x 的数, 并更新为 -1, 返回这个数的下标(没有则返回 -1)
    def find_first_and_update(self, i: int, l: int, r: int, x: int) -> int:
        if self.max[i] < x:
            return -1
        if l == r:
            self.max[i] = -1
            return l
        mid = (l + r) // 2
        temp = self.find_first_and_update(i * 2 + 1, l, mid, x)
        if temp == -1:
            temp = self.find_first_and_update(i * 2 + 2, mid + 1, r, x)
        self.maintain(i)
        return i