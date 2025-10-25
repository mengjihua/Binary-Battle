from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
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

def lexGreaterPermutation(s: str, target: str) -> str:
        n = len(s)
        cnt = Counter(s)
        
        def dfs(idx):
            if idx == n:
                return ''
            
            for c in sorted(cnt):
                if cnt[c] == 0:
                    continue
                
                if c < target[idx]:
                    continue
                elif c == target[idx]:
                    cnt[c] -= 1
                    suf = dfs(idx + 1)
                    if suf != '':
                        return c + suf
                    cnt[c] += 1
                else:
                    cnt[c] -= 1
                    return c + ''.join(sorted(cnt.elements()))
            return ''
        
        ans = dfs(0)
        
        return ans

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            cnt = Counter(str(n))
            if all(int(d) == c for d, c in cnt.items()):
                return n


if __name__ == "__main__":
    s = Solution()
    print(s.nextBeautifulNumber(n = 1000))