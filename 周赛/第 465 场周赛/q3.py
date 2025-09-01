from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
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
    def maxProduct(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        
        nums_set = set(nums)
        max_product = -inf
        
        for num1 in nums:
            comp = ((1 << 20) - 1) ^ num1
            temp = comp
            while True:
                if temp in nums_set:
                    num2 = temp
                    if num1 != num2 or cnt[num1] > 1:
                        max_product = max(max_product, num1 * num2)
                if temp == 0:
                    break
                temp = (temp - 1) & comp

        return max_product
    
    def maxProduct(self, nums: List[int]) -> int:
        mx = 1 << 20
        max_num = [0] * mx
        for x in nums:
            max_num[x] = x
        
        dp = max_num.copy()
        for i in range(20):
            for mask in range(mx):
                if mask & (1 << i):
                    temp = mask ^ (1 << i)
                    if dp[temp] > dp[mask]:
                        dp[mask] = dp[temp]
        
        ans = 0
        temp = mx - 1
        for s in range(mx):
            if max_num[s] != 0:
                comp = temp & (~s)
                if dp[comp] != 0:
                    product = max_num[s] * dp[comp]
                    if product > ans:
                        ans = product
        return ans
    

# print((1 << 20) * 20)