from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, pairwise
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, comb, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7


def int_to_ip(num: int) -> str:
    return ".".join([
        str((num >> 24) & 255),
        str((num >> 16) & 255),
        str((num >> 8) & 255),
        str(num & 255)
    ])

class Solution:
    def ipToCIDR(self, ip: str, n: int) -> List[str]:
        parts = list(map(int, ip.split('.')))
        curr_ip = (parts[0] << 24) | (parts[1] << 16) | (parts[2] << 8) | parts[3]
        res = []

        while n > 0:
            if curr_ip == 0: mx1 = 1 << 32
            else: mx1 = curr_ip & -curr_ip

            mx2 = 1
            while mx2 * 2 <= n: mx2 *= 2
            
            cover = min(mx1, mx2)
            
            k = cover.bit_length() - 1
            pre_len = 32 - k

            res.append(f"{int_to_ip(curr_ip)}/{pre_len}")

            curr_ip += cover
            n -= cover

        return res