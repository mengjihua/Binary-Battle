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
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        set_banned = set(banned)
        ans = 0
        for i in range(1, n + 1):
            if i not in set_banned:
                if maxSum >= i:
                    maxSum -= i
                    ans += 1
                else: break
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.maxCount(banned = [1,6,5], n = 5, maxSum = 6))