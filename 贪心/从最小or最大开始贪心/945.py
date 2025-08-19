from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def minIncrementForUnique(self, nums: List[int]) -> int:
    #     nums.sort()
    #     temp, ans = -1, 0
    #     for num in nums:
    #         if num <= temp:
    #             ans += temp - num + 1
    #             temp += 1
    #         else:
    #             temp = num
    #     return ans
    
    def minIncrementForUnique(self, nums: List[int]) -> int:
        heapify(nums)
        temp, ans = -1, 0
        while nums:
            num = heappop(nums)
            if num <= temp:
                ans += temp - num + 1
                temp += 1
            else:
                temp = num
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minIncrementForUnique(nums = [3,2,1,2,1,7]))