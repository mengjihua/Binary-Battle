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
    def countGood(self, nums: List[int], k: int) -> int:
        ans = r = temp = 0
        window = defaultdict(int)
        for l in range(len(nums)):
            while r < len(nums) and temp < k:
                temp += window[nums[r]]
                window[nums[r]] += 1
                r += 1
            if temp >= k:
                ans += len(nums) - r + 1
            window[nums[l]] -= 1
            temp -= window[nums[l]]
            if window[nums[l]] == 0:
                del window[nums[l]]
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.countGood(nums = [1,1,1,1,1], k = 10))
    print(s.countGood(nums = [3,1,4,3,2,2,4], k = 2))