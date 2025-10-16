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
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = defaultdict(int)
        for num in nums:
            cnt[(num % value + value) % value] += 1
            
        i = 0
        while True:
            if cnt[i % value] > 0:
                cnt[i % value] -= 1
                i += 1
            else:
                return i
            
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        cnt = [0] * value
        for num in nums:
            cnt[num % value] += 1
            
        i = 0
        while True:
            if cnt[i % value] > 0:
                cnt[i % value] -= 1
                i += 1
            else:
                return i
            
if __name__ == '__main__':
    s = Solution()
    print(s.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 5))
    print(s.findSmallestInteger(nums = [1,-10,7,13,6,8], value = 7))