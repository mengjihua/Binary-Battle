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

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1
        
        def check(time):
            cnt, temp = 0, 0
            for i in range(n):
                if bloomDay[i] > time:
                    temp = 0
                    continue
                temp += 1
                if temp == k:
                    cnt += 1
                    temp = 0
            return cnt >= m
                
        
        l, r = 0, max(bloomDay)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.minDays(bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3))