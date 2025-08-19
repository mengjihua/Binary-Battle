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
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans, r, n = 0, 0, len(nums)
        temp = 0
        for l in range(n):
            while r < n and temp & nums[r] == 0:
                temp |= nums[r]
                r += 1
            ans = max(ans, r - l)
            print(f'l = {l}, r = {r}, temp = {temp}')
            temp ^= nums[l]
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestNiceSubarray(nums=[1, 3, 8, 48, 10]))
    print(s.longestNiceSubarray(nums = [3,1,5,11,13]))
