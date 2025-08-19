from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(2 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        cnt = 0
        last_num = nums[0]
        i = 1
        while i < len(nums) - 1:
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1
            if i >= len(nums) - 1:
                break
            if nums[i] > last_num and nums[i] > nums[i + 1]:
                cnt += 1
            elif nums[i] < last_num and nums[i] < nums[i + 1]:
                cnt += 1
            last_num = nums[i]
            i += 1
        return cnt