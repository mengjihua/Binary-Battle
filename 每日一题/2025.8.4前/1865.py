from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums1)
        self.count1 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        # print('test')
        self.count1[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.count1[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        cnt = 0
        for num1, cnt1 in self.count2.items():
            cnt += cnt1 * self.count1[tot - num1]
        return cnt