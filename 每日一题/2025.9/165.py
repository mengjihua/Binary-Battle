from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = list(map(int, version1.split('.')))
        nums2 = list(map(int, version2.split('.')))

        n, m = len(nums1), len(nums2)
        if n > m:
            nums2.extend([0] * (n - m))
        elif m > n:
            nums1.extend([0] * (m - n))
        
        l = fmax(n, m)
        for i in range(l):
            if nums1[i] < nums2[i]:
                return -1
            elif nums1[i] > nums2[i]:
                return 1
        
        return 0