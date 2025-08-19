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
    def minArraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        dp = [0] * (n + 1)
        s = 0
        pre_sum_dic = {0: 0}
        
        pre_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            pre_sum[i] = pre_sum[i - 1] + nums[i - 1]
        
        for i in range(n):
            s = (s + nums[i]) % k

            dp[i + 1] = dp[i]
            if s in pre_sum_dic:
                j = pre_sum_dic[s]
                dp[i + 1] = max(dp[i], dp[j] + pre_sum[i + 1] - pre_sum[j])
            
            pre_sum_dic[s] = i + 1
        return sum(nums) - dp[n]
    

if __name__ == '__main__':
    s = Solution()
    print(s.minArraySum(nums = [3,1,4,1,5], k = 3))