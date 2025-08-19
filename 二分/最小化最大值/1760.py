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
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        n = len(nums)
        
        def check(x):
            cnt = 0
            for num in nums:
                # ceil(a / b) == (a - 1) // b + 1
                # => ceil(a / b) - 1 == (a - 1) // b
                cnt += (num - 1) // x
            return  cnt <= maxOperations
        
        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.minimumSize(nums = [9], maxOperations = 2))
    print(s.minimumSize(nums = [2,4,8,2], maxOperations = 4))