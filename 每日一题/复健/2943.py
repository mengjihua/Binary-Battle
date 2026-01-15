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

def get_max_consecutive(lst):
    res = cur_len = 1
    for i in range(1, len(lst)):
        if lst[i - 1] == lst[i] - 1:
            cur_len += 1
        else:
            cur_len = 1
        res = fmax(res, cur_len)
    return res

class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        h_len = h_cur_len = 1
        h_cur = hBars[0]
        for h in hBars[1:]:
            if h_cur == h - 1:
                h_cur_len += 1
            else:
                h_cur_len = 1
            h_cur = h
            h_len = fmax(h_len, h_cur_len)
        
        v_len = v_cur_len = 1
        v_cur = vBars[0]
        for v in vBars[1:]:
            if v_cur == v - 1:
                v_cur_len += 1
            else:
                v_cur_len = 1
            v_cur = v
            v_len = fmax(v_len, v_cur_len)
        
        return (fmin(v_len, h_len) + 1) ** 2
    
    
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        hBars.sort()
        vBars.sort()
        return (fmin(get_max_consecutive(hBars), get_max_consecutive(vBars)) + 1) ** 2
    
    
if __name__ == "__main__":
    s = Solution()
    print(s.maximizeSquareHoleArea(n = 2, m = 3, hBars = [2,3], vBars = [2,4]))