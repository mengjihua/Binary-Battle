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
    def maxArrayValue(self, nums: List[int]) -> int:
        ans, n = nums[-1], len(nums)
        
        for i in range(n - 1, 0, -1):
            # print(nums[i], nums[i - 1], ans)
            if ans >= nums[i - 1]:
                ans += nums[i - 1]
            else:
                ans = nums[i - 1]
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.maxArrayValue(nums = [2,3,7,9,3]))