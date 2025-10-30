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
    def countValidSelections(self, nums: List[int]) -> int:
        def move(nums: List[int], idx: int, direction: int, sm: int) -> bool:
            n = len(nums)
            cur = idx
            while 0 <= cur < n:
                if nums[cur] == 0:
                    cur += direction
                else:
                    nums[cur] -= 1
                    direction *= -1
                    cur += direction
                    sm -= 1
                if sm == 0:
                    return True
            return False
        
        sm = sum(nums)
        
        n = len(nums)
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                if move(nums.copy(), i, 1, sm):
                    ans += 1
                if move(nums.copy(), i, -1, sm):
                    ans += 1
        return ans
    

if __name__ == "__main__":
    s = Solution()
    print(s.countValidSelections(nums = [1,0,2,0,3]))