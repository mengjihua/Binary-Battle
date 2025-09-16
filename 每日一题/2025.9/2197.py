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

def lcm(a, b): return a * b // gcd(a, b)

class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        for i in range(n):
            while stack and gcd(stack[-1], nums[i]) > 1:
                nums[i] = lcm(stack.pop(), nums[i])
            stack.append(nums[i])
        return stack