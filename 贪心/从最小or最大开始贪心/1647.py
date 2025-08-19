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
    def minDeletions(self, s: str) -> int:
        lst = [0] * 26
        for c in s:
            lst[ord(c) - ord('a')] += 1
        lst.sort(reverse=True)
        
        ans, last_num = 0, float('inf')
        for num in lst:
            if num == 0: break
            if num >= last_num:
                ans += min(num, num - last_num + 1)
                last_num = max(0, last_num - 1)
            else:
                last_num = num
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.minDeletions(s = "bbcebab"))