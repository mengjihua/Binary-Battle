from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10 ** 5 + 1)
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        st = set(num for num in nums if num >= 0)
        return sum(st) if st else max(nums)