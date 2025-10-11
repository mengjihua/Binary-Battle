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
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        nums_cnt = sorted(cnt.items(), key=lambda x: x[0])
        # print(nums_cnt)
        
        n = len(nums_cnt)
        dp = [[0] * 2 for _ in range(n + 1)]
        for i in range(1, n + 1):
            num, c = nums_cnt[i - 1]
            dp[i][0] = max(dp[i - 1])  # 不选
            dp[i][1] = num * c  # 选
            # for j in range(max(1, i - 3), i):
            #     if num - 2 <= nums_cnt[j - 1][0]:
            #         break
            #     dp[i][1] = max(dp[i][1], max(dp[j]) + num * c)  # 选
            j = i - 1  # 倒着找第一个小于 num - 2 的位置, 这样就不用每次都从头找了
            while j and nums_cnt[j - 1][0] >= num - 2:
                j -= 1
            dp[i][1] += max(dp[j]) if j >= 0 else 0
                
        # print(dp)
        return max(dp[-1])
    
    # 合并状态(选|不选)
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        nums_cnt = sorted(cnt.items(), key=lambda x: x[0])
        
        n = len(nums_cnt)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            num, c = nums_cnt[i - 1]
            j = i - 1
            while j and nums_cnt[j - 1][0] >= num - 2:
                j -= 1
            if j >= 0:
                dp[i] = fmax(dp[i - 1], dp[j] + num * c)
            else:
                dp[i] = fmax(dp[i - 1], num * c)
                
        return dp[-1]
    
    # 记忆化搜索
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        nums_cnt = sorted(cnt.items(), key=lambda x: x[0])
        
        @lru_cache(maxsize=None)
        def dfs(i):
            if i < 0: return 0
            num, cnt = nums_cnt[i]
            j = i
            while j and nums_cnt[j - 1][0] >= num - 2:
                j -= 1
            return fmax(dfs(i - 1), dfs(j - 1) + num * cnt)

        return dfs(len(nums_cnt) - 1)
    
    # 双指针
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        nums_cnt = sorted(cnt.items(), key=lambda x: x[0])
        
        n = len(nums_cnt)
        dp = [0] * (n + 1)
        l = 0
        for r in range(n):
            num, cnt = nums_cnt[r]
            while nums_cnt[l][0] < num - 2:
                l += 1
            dp[r + 1] = max(dp[r], dp[l] + num * cnt)
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.maximumTotalDamage(power = [1,1,3,4]))
    # print(s.maximumTotalDamage(power = [7,1,6,6]))