from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans, l = 0, 0
        max_q, min_q = deque(), deque()
        for r in range(len(nums)):
            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()
            max_q.append(r)
            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()
            min_q.append(r)
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                if max_q[0] <= l:
                    max_q.popleft()
                if min_q[0] <= l:
                    min_q.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans
