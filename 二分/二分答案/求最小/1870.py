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
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) > ceil(hour):
            return -1

        def check(speed):
            need_time = 0
            for d in dist[:-1]:
                need_time += ceil(d / speed)
            need_time += dist[-1] / speed
            return need_time <= hour
        
        h = hour * 100 % 100 if hour != int(hour) else 100
        l, r = 1, ceil(max(dist) * 100 / h)
        while l <= r:
            mid = (l + r) // 2
            if check(mid) :
                r = mid - 1
            else:
                l = mid + 1
        return l

# if __name__ == '__main__':
#     s = Solution()
#     print(s.minSpeedOnTime(dist = [1,3,2], hour = 2.7))