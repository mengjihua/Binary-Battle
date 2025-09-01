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
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0
        
        # dp[i] 表示：游戏结束时，Alice 的分数 恰好为 i 的概率
        dp = [0.0] * (n + 1)
        dp[0] = 1.0
        
        # window_sum 维护的是 j ~ [i - maxPts, i - 1] 范围内所有 dp[j] 的和
        window_sum = 1.0  # 初始时只有 dp[0] 在窗口中
        
        # ans: 累加所有终止状态中分数 <= n 的概率（实际上只累加 >= k 的状态）
        ans = 0.0
        
        # 从分数 1 开始递推到 n
        for i in range(1, n + 1):
            # 当前分数 i 可以从 [i - maxPts, i - 1] 这些状态转移而来
            # 每个状态转移的概率是 1 / maxPts
            dp[i] = window_sum / maxPts
            
            # 如果当前分数 i >= k，游戏在此停止，这是一个终止状态
            if i >= k:
                ans += dp[i]
            else: # 如果当前分数 i < k，说明还能继续抽牌，因此 dp[i] 可以作为后续状态的来源
                window_sum += dp[i]
            
            # 维护滑动窗口大小为 maxPts
            # 此时dp[i - maxPts] 已经不在窗口 [i - maxPts + 1, i] 的左边边界外, 移除
            if i - maxPts >= 0:
                window_sum -= dp[i - maxPts]
        
        return ans