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
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        pre = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, 26):
                pre[i][(i - j) % 26] = pre[i][(i - j + 1) % 26] + previousCost[(i - j + 1) % 26]
        
        nxt = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for j in range(1, 26):
                nxt[i][(i + j) % 26] = nxt[i][(i + j - 1) % 26] + nextCost[(i + j - 1) % 26]
        
        ans = 0
        for c1, c2 in zip(s, t):
            ord1, ord2 = ord(c1) - ord('a'), ord(c2) - ord('a')
            ans += min(pre[ord1][ord2], nxt[ord1][ord2])
        return ans
    
    def shiftDistance(self, s: str, t: str, nextCost: List[int], previousCost: List[int]) -> int:
        pre = [0] * 26
        for i in range(25, -1, -1):
            pre[i] = pre[(i + 1) % 26] + previousCost[(i + 1) % 26]
        nxt = [0] * 26
        for i in range(26):
            nxt[i] = nextCost[(i - 1) % 26] + nxt[(i - 1) % 26]
        # print(pre, nxt)
            
        ans = 0
        for c1, c2 in zip(s, t):
            ord1, ord2 = ord(c1) - ord('a'), ord(c2) - ord('a')
            pc = (pre[ord2] - pre[ord1]) if ord1 >= ord2 else (pre[ord2] + pre[0] - pre[ord1])
            nc = (nxt[ord2] - nxt[ord1]) if ord1 <= ord2 else (nxt[25] - nxt[ord1] + nxt[ord2])
            # print(ord1, ord2, pc, nc)
            ans += _min(pc, nc)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.shiftDistance(s = "abab", t = "baba", 
                          nextCost = [100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0], 
                          previousCost = [1,100,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))