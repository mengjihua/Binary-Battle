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
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        temp1, temp2, n = 0, 0, len(nums)
        if n == 1:
            return 0
        for i in range(1, n - 1, 2):
            temp1 += max(0, nums[i] - nums[i - 1] + 1, nums[i] - nums[i + 1] + 1)
        temp2 += max(0, nums[0] - nums[1] + 1)
        for i in range(2, n - 1, 2):
            temp2 += max(0, nums[i] - nums[i - 1] + 1, nums[i] - nums[i + 1] + 1)
        # print([nums[i] for i in range(1, n - 1, 2)], [nums[i] for i in range(0, n - 1, 2)])
        # print(temp1, temp2)
        if n % 2 == 0:
            temp1 += max(0, nums[n - 1] - nums[n - 2] + 1)
        else:
            temp2 += max(0, nums[n - 1] - nums[n - 2] + 1)
        # print(temp1, temp2)
        return min(temp1, temp2)

if __name__ == "__main__":
    s = Solution()
    # print(s.movesToMakeZigzag(nums = [1,2,3]))
    print(s.movesToMakeZigzag(nums = [9,6,1,6,2]))