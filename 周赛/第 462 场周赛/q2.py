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
    def sortPermutation(self, nums: List[int]) -> int:
        pos = {num: i for i, num in enumerate(nums)}
        
        k = -1
        for i in range(len(nums) - 1):
            if i == nums[i]:
                continue
            j = pos[i]
            nums[i], nums[j] = nums[j], nums[i]
            pos[nums[i]], pos[nums[j]] = i, j
            if k == -1:
                k = nums[i] & nums[j]
            elif (nums[i] & nums[j]) | k != k:
                k &= nums[i] & nums[j]
        return k if k != -1 else 0

if __name__ == "__main__":
          s = Solution()
          print(s.sortPermutation(nums = [0,2,3,1]))