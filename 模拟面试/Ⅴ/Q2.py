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

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(depth: str, cnt1, cnt2):
            if len(depth) == 2 * n:
                ans.append(depth)
                return
            
            if cnt1 < n:
                dfs(depth + '(', cnt1 + 1, cnt2)
            if cnt2 < cnt1:
                dfs(depth + ')', cnt1, cnt2 + 1)

        dfs("", 0, 0)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))