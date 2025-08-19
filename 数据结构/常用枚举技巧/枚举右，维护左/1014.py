from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        
        pre = [0] * n
        pre[0] = values[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], values[i] + i)
        
        suff = [0] * n
        suff[n - 1] = values[n - 1] - (n - 1)
        for i in range(n - 2, -1, -1):
            suff[i] = max(suff[i + 1], values[i] - i)
        
        ans = max([pre[i] + suff[i + 1] for i in range(n - 1)])
        return ans
    
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        
        pre = [0] * n
        pre[0] = values[0]
        for i in range(1, n):
            pre[i] = max(pre[i - 1], values[i] + i)
        
        max_suff, ans = -inf, -inf
        for i in range(n - 1, 0, -1):
            max_suff = max(max_suff, values[i] - i)
            ans = max(ans, pre[i - 1] + max_suff)
        return ans
    
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_pre, ans = -inf, -inf
        for idx, num in enumerate(values):
            ans = max(ans, max_pre + num - idx)
            max_pre = max(max_pre, num + idx)
        return ans