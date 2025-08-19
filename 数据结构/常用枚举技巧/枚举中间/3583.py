from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        suf_cnt = defaultdict(int)
        for num in nums[:1:-1]:
            suf_cnt[num] += 1
        
        pre_cnt = defaultdict(int)
        pre_cnt[nums[0]] += 1
        
        ans = 0
        for i in range(1, len(nums) - 1):
            ans += pre_cnt[nums[i] * 2] * suf_cnt[nums[i] * 2]
            pre_cnt[nums[i]] += 1
            suf_cnt[nums[i + 1]] -= 1
        return ans % (10 ** 9 + 7)

    def specialTriplets(self, nums: List[int]) -> int:
        cnti = defaultdict(int)
        cntij = defaultdict(int)
        cntijk = 0
        for num in nums:
            if num % 2 == 0:
                cntijk += cntij[num // 2]
            cntij[num] += cnti[num * 2]
            cnti[num] += 1
        return cntijk % (10 ** 9 + 7)

if __name__ == '__main__':
    s = Solution()
    print(s.specialTriplets(nums = [6,3,6]))