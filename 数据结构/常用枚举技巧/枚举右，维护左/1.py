from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = defaultdict(int)
        for idx, num in enumerate(nums):
            if target - num in temp:
                return [temp[target - num], idx]
            else:
                temp[num] = idx

if __name__ == "__main__":
    s = Solution()
    print(s.twoSum(nums = [1, 2, 3, 4, 5], target = 3))