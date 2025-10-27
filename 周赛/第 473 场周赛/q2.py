from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, comb, sqrt, log, ceil, floor, inf
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
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(num) for num in nums]
        nums.sort(reverse=True)
        n = len(nums)
        # print(sum(nums[i] ** 2 for i in range(0, ceil(n / 2))), sum(-(nums[i] ** 2) for i in range(ceil(n / 2), n)))
        return sum(nums[i] ** 2 for i in range(0, ceil(n / 2))) + sum(-(nums[i] ** 2) for i in range(ceil(n / 2), n))
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxAlternatingSum(nums = [1,-1,2,-2,3,-3]))