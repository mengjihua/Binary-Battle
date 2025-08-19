from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
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
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        cnt = Counter(barcodes)
        items = sorted(cnt.items(), key=lambda x: -x[1])
        ans = []
        p, q = 0, 1
        p_cnt, q_cnt = items[p][1], items[q][1]
        while p < len(items):
            ans.extend([items[p][0], items[q][0]] * q_cnt)
            p_cnt -= q_cnt
            if q < len(items) - 1:
                if items[q + 1][1] <= p_cnt:
                    q += 1
                    q_cnt = items[q + 1][1]
                else:
                    q_cnt = p_cnt
                    p, q = q, p + 1
            else:
                ans.extend([items[p][0]] * p_cnt)
                break
        return ans