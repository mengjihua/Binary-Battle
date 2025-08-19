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
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + candiesCount[i - 1]
        
        ans = []
        for type_, day, cap in queries:
            day += 1
            if pre_sum[type_] != 0 and pre_sum[type_] % day == 0:
                min_eat = pre_sum[type_] // day + 1
            else:
                min_eat = ceil(pre_sum[type_] / day)
            ans.append(min_eat <= cap and day <= pre_sum[type_ + 1])
            # print(pre_sum[type_], pre_sum[type_ + 1], min_eat, max_eat)
        return ans
    
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(candiesCount)
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + candiesCount[i - 1]

        ans = []
        for type_, day, cap in queries:
            mn, mx = day + 1, (day + 1) * cap
            ans.append(pre_sum[type_] < mx and pre_sum[type_ + 1] >= mn)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.canEat(candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]))