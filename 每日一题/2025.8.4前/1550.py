from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 6 + 1)

class Solution:
    # def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    #     for i in range(len(arr) - 2):
    #         if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
    #             return True
    #     return False
    
    # 使用 any, all 函数简化
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(all(arr[i + j] % 2 == 1 for j in range(3)) for i in range(len(arr) - 2))