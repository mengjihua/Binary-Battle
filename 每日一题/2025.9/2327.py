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
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(1, n + 1):
            dp[i] %= MOD
            for j in range(i + delay, min(i + forget, n + 1)):
                dp[j] += dp[i]

        return sum(dp[-forget:]) % MOD
    
    def peopleAwareOfSecret1(self, n: int, delay: int, forget: int) -> int:
        '''使用差分数组优化, 时间复杂度 O(n)'''
        diff = [0] * (n + 1)
        diff[1], diff[2] = 1, -1
        ans = known = 0
        for i in range(1, n + 1):
            known = (known + diff[i]) % MOD
            if i >= n - forget + 1:
                ans += known
            if i + delay <= n:
                diff[i + delay] = (diff[i + delay] + known) % MOD
            if i + forget <= n:
                diff[i + forget] = (diff[i + forget] - known) % MOD
                
        return ans % MOD