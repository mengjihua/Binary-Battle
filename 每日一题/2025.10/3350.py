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

# 求从 start 开始的最长递增子数组的结束位置
def start2End(nums: List[int], start: int) -> int:
    n = len(nums)
    for i in range(start + 1, n):
        if nums[i] <= nums[i - 1]:
            return i - 1
    return n - 1

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        # 求单端最长递增子数组
        l = r = 0
        while r < n - 1:
            r = start2End(nums, l)
            ans = fmax(ans, (r - l + 1) // 2)
            l = r + 1
        # 求双端最长递增子数组的较小值, 即可行解 k
        l1, r1 = 0, start2End(nums, 0)
        l2, r2 = r1 + 1, start2End(nums, r1 + 1)
        ans = fmax(ans, fmin(r1 - l1 + 1, r2 - l2 + 1))
        while r2 < n - 1:
            l1, r1 = l2, r2
            l2, r2 = r2 + 1, start2End(nums, r1 + 1)
            ans = fmax(ans, fmin(r1 - l1 + 1, r2 - l2 + 1))
        return ans
    
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, start2End(nums, 0)
        last_l = r - l + 1  # 记录上一个单端最长递增子数组的长度
        ans = last_l // 2
        while r < n - 1:
            l, r = r + 1, start2End(nums, r + 1)
            ans = max(ans, fmin(r - l + 1, last_l), (r - l + 1) // 2)
            last_l = r - l + 1
        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.maxIncreasingSubarrays(nums = [2,5,7,8,9,2,3,4,3,1]))
    print(s.maxIncreasingSubarrays(nums = [1,2,3,4,4,4,4,5,6,7]))