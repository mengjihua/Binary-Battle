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
    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        temp = deque([i for i in range(n + 1)])
        ans = []
        for c in s:
            if c == 'I':
                ans.append(temp.popleft())
            else:
                ans.append(temp.pop())
        return ans + list(temp)

    def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        low, high = 0, n
        ans = []
        for c in s:
            if c == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1
        ans.append(low)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.diStringMatch("IDID"))
    print(s.diStringMatch("DDI"))
    print(s.diStringMatch("III"))