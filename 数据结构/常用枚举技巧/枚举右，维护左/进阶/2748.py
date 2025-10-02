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
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        def is_beautiful(x: int, y: int) -> bool:
            while x >= 10:
                x //= 10
            y %= 10
            return gcd(x, y) == 1
        
        return sum(is_beautiful(nums[i], nums[j]) for i in range(len(nums)) for j in range(i + 1, len(nums)))
    
    def countBeautifulPairs(self, nums: List[int]) -> int:
        n = len(nums)
        first, last = [0] * n, [0] * n
        for i in range(n):
            x = nums[i]
            while x >= 10:
                x //= 10
            first[i] = x
            last[i] = nums[i] % 10
        return sum(gcd(first[i], last[j]) == 1 for i in range(n) for j in range(i + 1, n))
    
    def countBeautifulPairs(self, nums: List[int]) -> int:
        is_beautiful = [[gcd(i, j) == 1 for j in range(10)] for i in range(10)]
        suf_last_sum = [0] * 10  # 记录后缀中各个位数结尾的数字个数
        
        for x in nums:
            suf_last_sum[x % 10] += 1
        
        ans = 0
        for x in nums:
            suf_last_sum[x % 10] -= 1
            first = x
            while first >= 10:
                first //= 10
            for last in range(1, 10):
                if is_beautiful[first][last]:
                    ans += suf_last_sum[last]
        return ans
    
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        pre_first_sum = [0] * 10  # 记录前缀中各个位数开头的数字个数
        for x in nums:
            for first, c in enumerate(pre_first_sum):
                if c and gcd(first, x % 10) == 1:
                    ans += c
            while x >= 10: 
                x //= 10
            pre_first_sum[x] += 1
        return ans