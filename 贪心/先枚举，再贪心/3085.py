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
MOD = 10 ** 9 + 7

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        word_cnt = sorted(Counter(word).values())
        mx, mx_save = word_cnt[-1], 0
        for base in range(mx + 1):
            mx_save = _max(mx_save, sum(_min(base + k, cnt) for cnt in word_cnt if cnt >= base))
        return sum(word_cnt) - mx_save
    
    def minimumDeletions(self, word: str, k: int) -> int:
        word_cnt = sorted(Counter(word).values())
        mx_save = 0
        for base in word_cnt:
            mx_save = _max(mx_save, sum(_min(base + k, cnt) for cnt in word_cnt if cnt >= base))
        return sum(word_cnt) - mx_save
        
    
if __name__ == '__main__':
    s = Solution()
    print(s.minimumDeletions(word = "aabcaba", k = 0))