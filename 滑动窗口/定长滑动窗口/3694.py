from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, pairwise
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, comb, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

d = {'U': 1j, 'D': -1j, 'L': -1, 'R': 1}
class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        n = len(s)
        preUD = [0] * (n + 1)
        preLR = [0] * (n + 1)
        
        for i in range(n):
            if s[i] == 'U':
                preUD[i + 1] = preUD[i] + 1
                preLR[i + 1] = preLR[i]
            elif s[i] == 'D':
                preUD[i + 1] = preUD[i] - 1
                preLR[i + 1] = preLR[i]
            elif s[i] == 'L':
                preUD[i + 1] = preUD[i]
                preLR[i + 1] = preLR[i] - 1
            else:
                preUD[i + 1] = preUD[i]
                preLR[i + 1] = preLR[i] + 1
        
        ans = set()
        for i in range(n - k + 1):
            ans.add(((preUD[i + k] - preUD[i]), (preLR[i + k] - preLR[i])))
        return len(ans)
    
    def distinctPoints(self, s: str, k: int) -> int:
        pre = list(accumulate([d[c] for c in s], initial=0))
        return len({q - p for q, p in zip(pre[k:], pre[:-k])})