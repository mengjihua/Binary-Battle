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
        n = len(nums)
        ans = 0
        
        for i in range(n):
            cnt0 = set()
            cnt1 = set()
            for j in range(i, n):
                num = nums[j]
                if num % 2 == 0:
                    cnt0.add(num)
                else:
                    cnt1.add(num)
                
                if len(cnt0) == len(cnt1):
                    ans = fmax(ans, j - i + 1)
    
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.longestBalanced(nums = [3,2,2,5,4]))
    print(s.longestBalanced(nums = [10,6,10,7]))