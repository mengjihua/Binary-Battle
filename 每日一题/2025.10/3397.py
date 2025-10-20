from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        cnt = sorted(list(Counter(nums).items()))
        mn_limit = -inf
        ans = 0
        for v, c in cnt:
            mn_exchange = fmax(mn_limit + 1, v - k)
            if mn_exchange <= v:
                c -= v - mn_exchange
                mx_change = v + fmin(c - 1, k)
            else:
                mx_change = fmin(mn_exchange + c - 1, v + k)
            ans += mx_change - mn_exchange + 1
            mn_limit = mx_change
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxDistinctElements(nums = [9,10,10,10,10,10,10,10,10], k = 3))  # 8