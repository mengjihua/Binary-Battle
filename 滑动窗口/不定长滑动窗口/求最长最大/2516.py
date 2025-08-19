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
    def takeCharacters(self, s: str, k: int) -> int:
        count = Counter(s)
        if any(count[c] < k for c in 'abc'):
            return -1
        
        n = len(s)
        ans, r = float('inf'), n
        window = [0] * 3
        while window[0] < k or window[1] < k or window[2] < k:
            r -= 1
            window[ord(s[r]) - ord('a')] += 1
        ans = n - r
        
        for l in range(n):
            window[ord(s[l]) - ord('a')] += 1
            while r < n and (window[0] >= k and window[1] >= k and window[2] >= k):
                window[ord(s[r]) - ord('a')] -= 1
                r += 1
            if r < n:
                ans = min(ans, n - r + l + 2)
            elif window[0] >= k and window[1] >= k and window[2] >= k:
                ans = min(ans, n - r + l + 1)
        return ans

    def takeCharacters(self, s: str, k: int) -> int:
        window = Counter(s)
        if any(window[c] < k for c in 'abc'):
            return -1

        n, ans, l = len(s), float('inf'), 0
        for r in range(n):
            window[s[r]] -= 1
            while window[s[r]] < k:
                window[s[l]] += 1
                l += 1
            ans = min(ans, n - (r - l + 1))
        return ans
    
if __name__ == "__main__":
    s = Solution()
    # print(s.takeCharacters(s = "aabaaaacaabc", k = 2))
    print(s.takeCharacters(s = "aabbccca", k = 2))