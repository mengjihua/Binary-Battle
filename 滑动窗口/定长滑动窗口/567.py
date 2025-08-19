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
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s2), len(s1)
        if m > n:
            return False

        cnt = Counter(s1)
        window = defaultdict(int)
        for r in range(n):
            window[s2[r]] += 1
            l = r - m + 1
            if l < 0:
                continue
            # print(f'l : {l}, r : {r}, window : {window}')
            if window == cnt:
                return True
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]
        return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print(Solution().checkInclusion(s1, s2))
