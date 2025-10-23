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
    def buildArray(self, target: List[int], n: int) -> List[str]:
        cur = 1
        ans = []
        for num in target:
            ans.append('Push')
            diff = num - cur
            if diff > 0:
                ans.extend(['Pop', 'Push'] * diff)
            cur = num + 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.buildArray(target = [1,3], n = 3))