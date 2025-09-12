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
    def reorganizeString(self, s: str) -> str:
        c_cnt_map = sorted(list(Counter(s).items()), key=lambda x: -x[1])
        n, m = len(s), max(c_cnt_map, key=lambda x: x[1])[1]
        
        if m > n - m + 1:
            return ""
        
        ans = [''] * n
        idx = 0
        for c, cnt in c_cnt_map:
            for _ in range(cnt):
                ans[idx] = c
                idx += 2
                if idx >= n:
                    idx = 1
        
        return ''.join(ans)
        

if __name__ == "__main__":
    s = Solution()
    print(s.reorganizeString('aabbcc'))
    # print(s.reorganizeString('aaab'))
    print(s.reorganizeString("vvvlo"))