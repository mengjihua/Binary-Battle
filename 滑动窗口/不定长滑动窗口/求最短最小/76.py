from typing import List, Tuple, Optional
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
    # def minWindow(self, s: str, t: str) -> str:
    #     ans, min_len, l = "", float('inf'), 0
    #     need = Counter(t)
    #     window = defaultdict(int)
    #     for r, c in enumerate(s):
    #         window[c] += 1
    #         while all((window[c] >= need[c] if s[l] != c else window[c] >= need[c] + 1) for c in need):
    #             window[s[l]] -= 1
    #             l += 1
    #         # print(f'l: {r}, {l}, {s[l:r + 1]}')
    #         if all(window[c] >= need[c] for c in need) and r - l + 1 < min_len:
    #             ans = s[l:r + 1]
    #             min_len = r - l + 1
    #     return ans
    
    def minWindow(self, s: str, t: str) -> str:
        ans, min_len, l, temp, n = "", float('inf'), 0, 0, len(s)
        need = Counter(t)
        window = defaultdict(int)
        
        for r, c in enumerate(s):
            window[c] += 1
            if window[c] == need[c]:
                temp += 1
                
            while l < n and window[s[l]] >= need[s[l]] + 1:
                # print(f'r: {r}, l: {l}, window: {s[l:r + 1]}, window[s[l]]: {window[s[l]]}, need[s[l]]: {need[s[l]]}')
                window[s[l]] -= 1
                l += 1
                
            if temp == len(need) and r - l + 1 < min_len:
                ans = s[l:r + 1]
                min_len = r - l + 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))