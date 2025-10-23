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
    def maxFrequency_weakenedVersion(self, nums: List[int], amplitude: int) -> int:
        cnt = sorted(Counter(nums).items(), key=lambda x: x[0])

        diff = [0] * (max(nums) + amplitude * 2 + 2)
        for k, c in cnt:
            diff[k] += c
            diff[k + amplitude * 2 + 1] -= c
        
        pre = list(accumulate(diff))
        return max(pre)
    
    def maxFrequency(self, nums: List[int], amplitude: int, numOperations: int) -> int:
        cnt = defaultdict(int)
        diff = defaultdict(int)
        for num in nums:
            cnt[num] += 1
            diff[num]
            diff[num - amplitude] += 1
            diff[num + amplitude + 1] -= 1

        ans = sum_d = 0
        for num, d in sorted(diff.items()):
            sum_d += d
            ans = fmax(ans, fmin(sum_d, cnt[num] + numOperations))
        return ans