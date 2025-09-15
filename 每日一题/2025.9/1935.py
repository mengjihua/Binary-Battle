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
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        set_broken = set(brokenLetters)
        ans = 0
        for word in words:
            if any(c in set_broken for c in word):
                continue
            ans += 1
        return ans
    
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        mask = 0
        for c in brokenLetters:
            mask |= 1 << (ord(c) - ord('a'))
            
        ans = 0
        for word in text.split():
            if any((mask >> (ord(c) - ord('a'))) & 1 for c in word):
                continue
            ans += 1
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.canBeTypedWords(text = "hello world", brokenLetters = "ad"))