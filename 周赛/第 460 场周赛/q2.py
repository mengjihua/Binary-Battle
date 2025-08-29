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
setrecursionlimit(2 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b

class Solution:
    def numOfSubsequences(self, s: str) -> int:
        set_s = set(s)
        if ('L' not in set_s and 'C' not in set_s) or ('C' not in set_s and 'T' not in set_s) or ('L' not in set_s and 'T' not in set_s):
            return 0
        n = len(s)
         
        pre_L = [0] * (n + 1)
        for i in range(n):
            pre_L[i + 1] = pre_L[i] + (1 if s[i] == 'L' else 0)
         
        suf_T = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suf_T[i] = suf_T[i + 1] + (1 if s[i] == 'T' else 0)
         
        LCT_num = 0
        for i in range(n):
            if s[i] == 'C':
                LCT_num += pre_L[i] * suf_T[i]
        
        best = LCT_num
         
        add_L = 0
        for i in range(n):
            if s[i] == 'C':
                add_L += suf_T[i]
        best = max(best, LCT_num + add_L)
        
        add_T = 0
        for i in range(n):
            if s[i] == 'C':
                add_T += pre_L[i]
        best = max(best, LCT_num + add_T)
        
        add_C = 0
        for i in range(n + 1):
            L_num = pre_L[i]    
            T_num = suf_T[i]
            add_C = max(add_C, L_num * T_num)
        best = max(best, LCT_num + add_C)
        
        return best
    
if __name__ == '__main__':
    s = Solution()
    print(s.numOfSubsequences("TTGCLCEL"))