from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, pairwise
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
    # 解法错误, 贪心策略不对
    # def minCost(self, colors: str, neededTime: List[int]) -> int:
    #     n = len(colors)
    #     dp = [[inf, inf] for _ in range(n)]  # dp[i][0]: i 保留, dp[i][1]: i 删
    #     dp[0][0] = 0
    #     dp[0][1] = neededTime[0]
    #     for i in range(1, n):
    #         if colors[i] != colors[i - 1]:
    #             dp[i][0] = fmin(dp[i - 1][0], dp[i - 1][1])
    #         else:
    #             dp[i][0] = dp[i - 1][1]
    #         dp[i][1] = fmin(dp[i - 1][0], dp[i - 1][1]) + neededTime[i]
    #     print(dp)
    #     return fmin(dp[n - 1][0], dp[n - 1][1])
    
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = neededTime[0]
        mx_cost = neededTime[0]
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                ans += neededTime[i]
                mx_cost = fmax(mx_cost, neededTime[i])
            else:
                ans += neededTime[i] - mx_cost
                mx_cost = neededTime[i]
        return ans - mx_cost
    
if __name__ == "__main__":
    s = Solution()
    print(s.minCost(colors = "bbbaaa", neededTime = [4,9,3,8,8,9]))