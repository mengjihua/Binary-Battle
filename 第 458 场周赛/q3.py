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
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        lens = [0] * (n + 1)

        for i in range(n):
            c = s[i]
            if c.isalpha():
                lens[i + 1] = lens[i] + 1
            elif c == '*':
                lens[i + 1] = max(lens[i] - 1, 0)
            elif c == '#':
                lens[i + 1] = lens[i] * 2
            elif c == '%':
                lens[i + 1] = lens[i]

        if k >= lens[n]:
            return '.'

        idx = k
        for i in range(n, 0, -1):
            c = s[i - 1]
            if c.isalpha():
                if lens[i] - 1 == idx:
                    return c
            elif c == '*':
                if lens[i] < lens[i - 1]:
                    idx += 1
            elif c == '#':
                if idx >= (lens[i] // 2):
                    idx -= (lens[i] // 2)
                else:
                    pass  # 前半段不需要变化
            elif c == '%':
                idx = lens[i] - 1 - idx

        return '.'  # 兜底

if __name__ == "__main__":
    s = Solution()
    print(s.processStr(s = "a#b%*", k = 1))
    print(s.processStr(s = "cd%#*#", k = 3))