from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys
sys.setrecursionlimit(10 ** 5 + 1)

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr: List[int]):
        self.arr = arr
    
    def get(self, index: int) -> int:
        return self.arr[index]
   
    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def get_peak():
            l, r = 1, mountainArr.length() - 2
            while l <= r:
                mid = (l + r) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        def search(l, r, asc):
            while l <= r:
                mid = (l + r) // 2
                val = mountainArr.get(mid)
                if val == target: return mid
                if asc ^ (val < target): r = mid - 1
                else: l = mid + 1
            return -1

        n = mountainArr.length()
        peak = get_peak()
        if mountainArr.get(peak) == target:
            return peak
        left = search(0, peak - 1, True)
        return left if left != -1 else search(peak + 1, n - 1, False)