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
    # def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    #     happiness.sort(reverse=True)
    #     ans = 0
    #     for i in range(k):
    #         ans += max(0, happiness[i] - i)
    #     return ans
    
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        neg_happiness = [-h for h in happiness]
        heapify(neg_happiness)
        ans = 0
        for i in range(k):
            ans += max(0, -heappop(neg_happiness) - i)
        return ans 