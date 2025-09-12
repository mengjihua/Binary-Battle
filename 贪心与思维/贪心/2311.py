from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 6 + 1)

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        s = s[::-1]
        temp, ans = 0, 0
        for i in range(len(s)):
            if s[i] == '1':
                temp += 1 << i
                if temp <= k:
                    ans += 1
            else:
                ans += 1
        return ans