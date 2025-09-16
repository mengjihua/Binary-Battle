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

class XorBasis:
    def __init__(self, n: int):
        """ 初始化一个大小为 n 的线性基 """
        self.b = [0] * n

    def insert(self, x: int) -> None:
        ''' 
            向线性基中插入一个数 x
            若 x 能被已有基表示，则不插入（线性相关）
            否则插入 x (线性无关)
        '''
        b = self.b
        for i in range(len(b) - 1, -1, -1):
            if x >> i:
                if b[i] == 0:
                    b[i] = x
                    return True
                x ^= b[i]
        return False

    def max_xor(self) -> int:
        ''' 返回线性基能表示的最大异或和 '''
        b = self.b
        res = 0
        for i in range(len(b) - 1, -1, -1):
            res = _max(res, res ^ b[i])
        return res
    
    