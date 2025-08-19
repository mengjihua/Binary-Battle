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
    #  s，它由小写英文字母和特殊字符：*、# 和 % 组成。
    def processStr(self, s: str) -> str:
        res = []
        for c in s:
            if c.isalpha():
                res.append(c)
            elif c == '*':
                if res:
                    res.pop()
            elif c == '#':
                if res:
                    res += res
            elif c == '%':
                if res:
                    res = res[::-1]
        return ''.join(res)