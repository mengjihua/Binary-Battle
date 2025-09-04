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
    def distance(self, nums: List[int]) -> List[int]:
        nums_idx_map = defaultdict(list)
        for idx, num in enumerate(nums):
            nums_idx_map[num].append(idx)
            
        arr = [0] * len(nums)
        for num, indices in nums_idx_map.items():
            s = list(accumulate(indices, initial=0))
            n = len(indices)
            for i, idx in enumerate(indices):
                arr[idx] = idx * i - s[i] + (s[-1] - s[i]) - (n - i) * idx

        return arr