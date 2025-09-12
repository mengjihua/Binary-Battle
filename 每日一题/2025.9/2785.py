from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiouAEIOU'
        temp = []
        ans = [''] * len(s)
        for idx, c in enumerate(s):
            if c not in vowels:
                ans[idx] = c
            else:
                temp.append(c)
        temp.sort()
        temp = deque(temp)
        for i in range(len(s)):
            if ans[i] == '':
                ans[i] = temp.popleft()
        return ''.join(ans)