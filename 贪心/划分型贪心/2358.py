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

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        # 1 + 2 + 3 + 4 + ... + n = (1 + n) * n // 2 <= len(grades)
        # -> n ** 2 + n <= 2 * len(grades)
        # -> n <= int(sqrt(2 * len(grades) + 0.25) - 0.5)
        return int(sqrt(2 * len(grades) + 0.25) - 0.5)