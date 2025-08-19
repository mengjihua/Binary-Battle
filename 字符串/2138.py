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
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [s[i:i + k].ljust(k, fill) for i in range(0, len(s), k)]