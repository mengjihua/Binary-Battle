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
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        def longest_common_prefix_length(s, t):
            k = 0
            min_len = min(len(s), len(t))
            while k < min_len and s[k] == t[k]:
                k += 1
            return k
        
        n = len(words)
        if n == 1:
            return [0]
        if n == 2:
            return [0, 0]
        
        lcp_orig = []
        for j in range(n - 1):
            a = words[j]
            b = words[j + 1]
            lcp_orig.append(longest_common_prefix_length(a, b))
        
        pref_max = [0] * (n - 1)
        pref_max[0] = lcp_orig[0]
        for i in range(1, n - 1):
            pref_max[i] = max(pref_max[i - 1], lcp_orig[i])
        
        suff_max = [0] * (n - 1)
        suff_max[n - 2] = lcp_orig[n - 2]
        for i in range(n - 3, -1, -1):
            suff_max[i] = max(lcp_orig[i], suff_max[i + 1])
        
        ans = [0] * n
        
        ans[0] = suff_max[1] if n >= 3 else 0
        
        if n >= 3:
            ans[n - 1] = pref_max[n - 3]
        
        for i in range(1, n - 1):
            if i - 2 >= 0:
                left_max_val = pref_max[i - 2]
            else:
                left_max_val = 0
            
            new_lcp_val = longest_common_prefix_length(words[i - 1], words[i + 1])
            
            if i + 1 <= n - 2:
                right_max_val = suff_max[i + 1]
            else:
                right_max_val = 0
            
            ans[i] = max(left_max_val, new_lcp_val, right_max_val)
        
        return ans
    
if __name__ == "__main__":
    s = Solution()
    print(s.longestCommonPrefix(["jump","run","run","jump","run"]))