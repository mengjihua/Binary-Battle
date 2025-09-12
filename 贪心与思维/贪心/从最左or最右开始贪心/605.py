from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return n <= 1
        ans = 1 if len(flowerbed) >= 2 and flowerbed[1] != 1 and flowerbed[0] == 0 else 0
        flowerbed[0] = flowerbed[0] if ans == 0 else 1
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i - 1] + flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                ans += 1
        print(flowerbed)
        return (ans + (1 if len(flowerbed) >= 2 and flowerbed[-2] != 1 and flowerbed[-1] == 0 else 0)) >= n