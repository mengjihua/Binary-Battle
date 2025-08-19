from typing import List, Tuple, Dict, Set, Optional
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
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10 ** 9 + 7
        sorted_nums1 = sorted(nums1)
        diff_sum = sum(abs(a - b) for a, b in zip(nums1, nums2))
        max_diff, n = 0, len(nums1)
        for a, b in zip(nums1, nums2):
            if a == b:
                continue
            idx = bisect_left(sorted_nums1, b)
            if idx < n:
                max_diff = max(max_diff, abs(a - b) - abs(sorted_nums1[idx] - b))
            if idx > 0:
                max_diff = max(max_diff, abs(a - b) - abs(sorted_nums1[idx - 1] - b))
        return (diff_sum - max_diff) % MOD


if __name__ == '__main__':
    s = Solution()
    print(s.minAbsoluteSumDiff(nums1=[1, 7, 5], nums2=[2, 3, 5]))
    # print(s.minAbsoluteSumDiff(
    #     nums1=[1, 10, 4, 4, 2, 7], nums2=[9, 3, 5, 1, 7, 4]))
