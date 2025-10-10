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
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        
        suf = [0] * (n + k)
        for i in range(n - 1, -1, -1):
            suf[i] = suf[i + k] + energy[i]
        return max(suf[:-k])
    
    # 空间优化
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        
        suf = [0] * k
        ans = -inf
        for i in range(n - 1, -1, -1):
            suf[i % k] = suf[(i + k) % k] + energy[i]
            ans = fmax(ans, suf[i % k])
        return ans
    
    # 原地修改
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)


if __name__ == '__main__':
    s = Solution()
    print(s.maximumEnergy(energy = [5,2,-10,-5,1], k = 3))