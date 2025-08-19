from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # 计算两者之和为偶数的最大子序列长度
        odd_count = sum(1 for num in nums if num % 2 == 1)
        even_count = len(nums) - odd_count
        ans1 = max(even_count, odd_count)
        # 计算两者之和为奇数的最大子序列长度
        ans2, last_num = 1, nums[0]
        for num in nums[1:]:
            if (last_num + num) % 2 == 1:
                ans2 += 1
                last_num = num
        return max(ans1, ans2)