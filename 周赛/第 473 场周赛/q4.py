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
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]
        
        pos = defaultdict(list)
        pos[0].append(0)
        vis = set()
        
        ans = 0
        for r in range(1, n + 1):
            cur_mod = pre[r] % k
            
            for l in pos[cur_mod]:
                sub = tuple(nums[l:r])
                if sub not in vis:
                    vis.add(sub)
                    ans += 1
            
            pos[cur_mod].append(r)
        
        return ans
    

if __name__ == "__main__":
    s = Solution()
    print(s.numGoodSubarrays(nums = [1,2,3], k = 3))
    print(s.numGoodSubarrays(nums = [2,2,2,2,2,2], k = 6))