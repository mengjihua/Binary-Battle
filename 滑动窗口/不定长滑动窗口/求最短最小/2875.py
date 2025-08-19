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
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        sum_num = sum(nums)
        cnt = len(nums) * (target // sum_num)
        target = target % sum_num
        if target == 0:
            return cnt
        
        nums = nums + nums
        ans, l = float('inf'), 0
        for r in range(len(nums)):
            target -= nums[r]
            while target + nums[l] <= 0:
                target += nums[l]
                l += 1
            if target == 0:
                ans = min(ans, r - l + 1)
        return ans + cnt if ans != float('inf') else -1

if __name__ == '__main__':
    s = Solution()
    print(s.minSizeSubarray(nums = [1,6,5,5,1,1,2,5,3,1,5,3,2,4,6,6], target = 56))