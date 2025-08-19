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
MOD = 10 ** 9 + 7

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        
        base = sum(strategy[i] * prices[i] for i in range(n))
        
        max_add = add = 0
        for j in range(k // 2):
            add -= strategy[j] * prices[j]
        for j in range(k // 2, k):
            add += (1 - strategy[j]) * prices[j]
        max_add = max(max_add, add)
        
        for i in range(1, n - k + 1):
            l, mid, r = i - 1, i + k // 2 - 1, i + k - 1
            add += strategy[l] * prices[l] + (1 - strategy[r]) * prices[r]
            add -=  prices[mid]
            max_add = max(max_add, add)
        
        return base + max_add
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit(prices = [4,2,8], strategy = [-1,0,1], k = 2))
    print(s.maxProfit(prices = [5,4,3], strategy = [1,1,0], k = 2))