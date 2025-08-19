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
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        temp, min_len, l = 0, float('inf'), 0
        for r in range(len(s)):
            temp += int(s[r])
            while temp - int(s[l]) >= k:
                temp -= int(s[l])
                l += 1
            if temp == k:
                min_len = min(min_len, r - l + 1)
                
        ans = ''
        l, temp = 0, 0
        for r in range(len(s)):
            temp += int(s[r])
            while temp - int(s[l]) >= k:
                temp -= int(s[l])
                l += 1
            if temp == k and r - l + 1 == min_len:
                ans = min(ans, s[l:r + 1]) if ans else s[l:r + 1]
        return ans if ans else ''

if __name__ == '__main__':
    s = Solution()
    print(s.shortestBeautifulSubstring(s = "100011001", k = 3))