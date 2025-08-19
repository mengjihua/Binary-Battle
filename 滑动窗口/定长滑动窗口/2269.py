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
    # def divisorSubstrings(self, num: int, k: int) -> int:
    #     str_num = str(num)
    #     cnt = 0
    #     for i in range(len(str_num) - k + 1):
    #         sub_sum = int(str_num[i:i + k])
    #         if sub_sum != 0 and num % sub_sum == 0:
    #             cnt += 1
    #     return cnt

    def divisorSubstrings2(self, num: int, k: int) -> int:
        mod = 10 ** k
        cnt, n = 0, num
        while n >= mod // 10:
            sub_sum = n % mod
            if sub_sum != 0 and num % sub_sum == 0:
                cnt += 1
            n //= 10
        return cnt