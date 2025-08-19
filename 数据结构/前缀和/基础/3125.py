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
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        pre = [0] * n
        pre[0] = 0
        for i in range(1, n):
            if nums[i] % 2 == nums[i - 1] % 2:
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = pre[i - 1]
                
        ans = []
        for l, r in queries:
            judge = True if pre[r] - pre[l] == 0 else False
            ans.append(judge)
        return ans