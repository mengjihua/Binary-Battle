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
    def makeFancyString(self, s: str) -> str:
        last_c, cnt = '', 0
        ans = []
        for c in s:
            if last_c != c:
                last_c = c
                cnt = 1
            else:
                cnt += 1
            if cnt == 3:
                cnt -= 1
                continue
            ans.append(c)
        return ''.join(map(str, ans))