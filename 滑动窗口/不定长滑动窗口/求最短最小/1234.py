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
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        n = len(s)
        
        if all(cnt[c] == n // 4 for c in 'QWER'):
            return 0
        
        for c in 'QWER':
            if cnt[c] > n // 4:
                cnt[c] = cnt[c] - n // 4
            else:
                cnt[c] = 0
        
        window = defaultdict(int)
        ans, l = n, 0
        for r in range(n):
            window[s[r]] += 1
            # while all(window[c] >= cnt[c] for c in 'QWER'):
            #     ans = min(ans, r - l + 1)
            #     window[s[l]] -= 1
            #     l += 1
            while all((window[c] >= cnt[c] if c != s[l] else window[c] - 1 >= cnt[c]) for c in 'QWER'):
                window[s[l]] -= 1
                l += 1
            if all(window[c] >= cnt[c] for c in 'QWER'):
                ans = min(ans, r - l + 1)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.balancedString(s = "QWER"))