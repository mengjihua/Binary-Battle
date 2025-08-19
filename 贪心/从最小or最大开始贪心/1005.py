from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys
sys.setrecursionlimit(10 ** 5 + 1)


class Solution:
    # def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
    #     nums.sort()
    #     ans, n = 0, len(nums)
    #     for i in range(n):
    #         if k > 0 and nums[i] < 0:
    #             ans += -nums[i]
    #             k -= 1
    #         elif k <= 0 or k % 2 == 0:
    #             return ans + sum(nums[i:])
    #         elif i - 1 >= 0 and nums[i] > abs(nums[i - 1]):
    #             return ans + sum(nums[i:]) + 2 * nums[i - 1]
    #         else:
    #             return ans + sum(nums[i:]) - 2 * nums[i]
    #     return ans if k % 2 == 0 else ans + 2 * nums[-1]

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while k and nums:
            if nums[0] < 0:
                heappush(nums, -heappop(nums))
                k -= 1
            else:
                if nums[0] > 0 and k % 2 == 1:
                    heappush(nums, -heappop(nums))
                break
        return sum(nums)


if __name__ == '__main__':
    s = Solution()
    print(s.largestSumAfterKNegations([-8, 3, -5, -3, -5, -2], 10 ** 9))
