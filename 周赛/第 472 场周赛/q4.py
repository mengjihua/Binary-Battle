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
    def longestBalanced(self, nums: List[int]) -> int:
        if all(num % 2 == 0 for num in nums) or all(num % 2 == 1 for num in nums):
            return 0
        
        n = len(nums)
        
        vis = set()
        pre = [0] * (n + 1)
        cur = 0
        for i in range(n):
            if nums[i] not in vis:
                if nums[i] % 2 == 0:
                    cur += 1
                else:
                    cur -= 1
                vis.add(nums[i])
            pre[i + 1] = cur
        
        pos = defaultdict(int)
        ans = 0
        for i in range(n + 1):
            if pre[i] not in pos:
                pos[pre[i]] = i
            else:
                ans = fmax(ans, i - pos[pre[i]])

        return ans
    
if __name__ == "__main__":
    s = Solution()
    # print(s.longestBalanced(nums = [3,2,2,5,4]))
    # print(s.longestBalanced(nums = [10,6,10,7]))
    # print(s.longestBalanced(nums = [6,6]))
    # print(s.longestBalanced(nums = [1,2,3,2]))
    print(s.longestBalanced(nums = [10,6,10,7]))