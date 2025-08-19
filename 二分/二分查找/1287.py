from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        # n = len(arr)
        # target_cnt = n // 4
        # cnt = defaultdict(int)
        # for num in arr:
        #     cnt[num] += 1
        #     if cnt[num] > target_cnt:
        #         return num
        # return -1
        m = len(arr) // 4
        for i in (m, m * 2 + 1):
            x = arr[i]
            j = bisect_left(arr, x)
            if arr[j + m] == x:
                return x
        return arr[m * 3 + 2]