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
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) <= 3:
            return False

        idx = 1
        while idx < len(nums) - 2:
            if nums[idx] > nums[idx - 1]:
                idx += 1
            else:
                break
        if idx == 1:
            return False
        
        temp = idx
        while idx < len(nums) - 1:
            if nums[idx] < nums[idx - 1]:
                idx += 1
            else:
                break
        if idx == temp:
            return False
        
        while idx < len(nums):
            if nums[idx] > nums[idx - 1]:
                idx += 1
            else:
                break
        
        return True if idx == len(nums) else False