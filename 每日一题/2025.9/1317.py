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
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n // 10 == 0:
            return [1, n - 1]

        sub = 0
        a, b = 0, 0
        pow_num = 0
        while n:
            digit = n % 10 - sub
            
            if n // 10 == 0:
                b = digit * 10 ** pow_num + b
                break
            
            if digit == -1:
                a = 1 * 10 ** pow_num + a
                b = 8 * 10 ** pow_num + b
                sub = 1
            elif digit == 0:
                a = 1 * 10 ** pow_num + a
                b = 9 * 10 ** pow_num + b
                sub = 1
            elif digit == 1:
                a = 2 * 10 ** pow_num + a
                b = 9 * 10 ** pow_num + b
                sub = 1
            else:
                a = 1 * 10 ** pow_num + a
                b = (digit - 1) * 10 ** pow_num + b
                sub = 0
            n //= 10
            pow_num += 1
        return [a, b]
    
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n // 10 == 0:
            return [1, n - 1]

        temp = n
        a = sub = pow_num = 0
        while temp:
            digit = temp % 10 - sub
            
            if temp // 10 == 0:
                a = digit * 10 ** pow_num + a
                break
            
            if digit in (-1, 0, 1):
                a = (digit + 2) * 10 ** pow_num + a
                sub = 1
            else:
                a = digit // 2 * 10 ** pow_num + a
                sub = 0
            temp //= 10
            pow_num += 1
        return [a, n - a]