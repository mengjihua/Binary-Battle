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
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def dfs(cur):
            if cur == target: return 1
            if cur > target: return 0
            return sum(dfs(cur + x) for x in nums)
        return dfs(0)
    
    # 有顺序
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i < num: continue
                dp[i] += dp[i - num]
        print(dp)
        return dp[target]
    
    # 无顺序, 答案错误
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for i in range(num, target + 1):
                dp[i] += dp[i - num]
        print(dp)
        return dp[target]
    

if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 4
    solution = Solution()
    print(solution.combinationSum4(nums, target)) 