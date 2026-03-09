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

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)
        
        def check(mid):
            workers = [0] * k
            
            def dfs(depth: int) -> bool:
                if depth == n:
                    return True
                
                cur = jobs[depth]
                
                for i in range(k):
                    if workers[i] + cur <= mid:
                        workers[i] += cur
                        if dfs(depth + 1):
                            return True
                        workers[i] -= cur
                    
                    if workers[i] == 0:
                        break
                    
                return False

            return dfs(0)

        l = jobs[0]
        res = r = sum(jobs)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res