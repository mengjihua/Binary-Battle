from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        mx = ans = 0
        
        diff = [0] * 101
        for birth, death in logs:
            diff[birth - 1950] += 1
            diff[death - 1950] -= 1

        pre = list(accumulate(diff))
        for i, cnt in enumerate(pre):
            if cnt > mx:
                mx = cnt
                ans = i
        return ans + 1950

if __name__ == "__main__":
    s = Solution()
    print(s.maximumPopulation([[1950, 1953], [1951, 1955]]))