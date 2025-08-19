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
    def minFlips(self, target: str) -> int:
        add = 0
        for ch in target:
            if add % 2 != (ch == '1'):
                add += 1
        return add

if __name__ == "__main__":
    s = Solution()
    print(s.minFlips(target = "001011101"))