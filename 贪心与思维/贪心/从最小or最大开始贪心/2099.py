from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 6 + 1)

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp = Counter(sorted(nums, reverse=True)[:k])
        ans = []
        for num in nums:
            if num in temp:
                ans.append(num)
                temp[num] -= 1
                if temp[num] == 0:
                    del temp[num]
        return ans