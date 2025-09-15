from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        max_freq = max(cnt.values())
        n = len(nums)
        if max_freq <= n - max_freq + 1:
            return n % 2
        return max_freq - (n - max_freq)
    
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        x = nums[n // 2]
        max_freq = bisect_right(nums, x) - bisect_left(nums, x)
        return max(n % 2, max_freq - (n - max_freq))
    
if __name__ == "__main__":
    s = Solution()
    print(s.minLengthAfterRemovals([1, 2, 4, 4, 4]))