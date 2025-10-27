from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
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
def lcm(a, b): return a * b // gcd(a, b,)
MOD = 10 ** 9 + 7

class Solution:
    def countStableSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        pos = defaultdict(lambda: defaultdict(list))
        for r, num in enumerate(nums):
            sm = pre[r]
            pos[num][sm].append(r)

        ans = 0
        for l, num in enumerate(nums[:-2]):
            temp = pre[l + 1] + num
            if num in pos and temp in pos[num]:
                lst = pos[num][temp]
                i = bisect_left(lst, l + 2)
                ans += len(lst) - i
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.countStableSubarrays([9,3,3,3,9]))