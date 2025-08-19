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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = l = cur_sum = 0
        for r in range(len(nums)):
            cur_sum += nums[r]
            while cur_sum * (r - l + 1) >= k:
                cur_sum -= nums[l]
                l += 1
            ans += r - l + 1
        return ans

# if __name__ == '__main__':
#     s = Solution()
#     print(s.countSubarrays(nums = [2,1,4,3,5], k = 10))
#     print(s.countSubarrays(nums = [1,1,1], k = 5))