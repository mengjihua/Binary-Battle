from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        ans = inf
        for i in range(n):
            for j in range(m):
                temp1 = landStartTime[i] + landDuration[i]
                if temp1 < waterStartTime[j]:
                    temp1 = waterStartTime[j] + waterDuration[j]
                else:
                    temp1 = temp1 + waterDuration[j]
                temp2 = waterStartTime[j] + waterDuration[j]
                if temp2 < landStartTime[i]:
                    temp2 = landStartTime[i] + landDuration[i]
                else:
                    temp2 = temp2 + landDuration[i]
                ans = min(ans, temp1, temp2)
        return ans