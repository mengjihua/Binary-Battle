from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1.sort(), s2.sort()
        return all(c1 >= c2 for c1, c2 in zip(s1, s2)) or all(c1 <= c2 for c1, c2 in zip(s1, s2))
    
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1_cnt, s2_cnt = Counter(s1), Counter(s2)
        
        def check(s1_cnt, s2_cnt):
            s1_pre, s2_pre = 0, 0
            for i in range(26):
                c = chr(i + ord('a'))
                s1_pre += s1_cnt[c]
                s2_pre += s2_cnt[c]
                if s1_pre > s2_pre:
                    return False
            return True
        
        return check(s1_cnt, s2_cnt) or check(s2_cnt, s1_cnt)

if __name__ == "__main__":
    s = Solution()
    print(s.checkIfCanBreak(s1 = "abe", s2 = "acd")) # False