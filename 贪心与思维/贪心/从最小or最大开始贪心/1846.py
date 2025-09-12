from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    #     arr.sort()
    #     temp = 1
    #     for num in arr[1:]:
    #         if abs(num - temp) > 1:
    #             temp = temp + 1
    #         else:
    #             temp = num
    #     return temp
    
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        n = len(arr)
        cnt = [0] * (n + 1)
        for num in arr:
            cnt[min(num, n)] += 1
        ans = 0
        for i in range(1, n + 1):
            ans = min(i, ans + cnt[i])
        return ans