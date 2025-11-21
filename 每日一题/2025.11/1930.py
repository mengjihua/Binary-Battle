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
    def countPalindromicSubsequence(self, s: str) -> int:
        suf_cnt = Counter(s[2:])
        
        pre_cnt = defaultdict(int)
        pre_cnt[s[0]] += 1
        # print(pre_cnt, suf_cnt)
        ans = set()
        for i in range(1, len(s) - 1):
            for j in range(26):
                c2 = chr(ord('a') + j)
                if pre_cnt[c2] > 0 and suf_cnt[c2] > 0:
                    ans.add(c2 + s[i] + c2)
            pre_cnt[s[i]] += 1
            suf_cnt[s[i + 1]] -= 1
        # print(ans)
        return len(ans) % (10 ** 9 + 7)
    
    def countPalindromicSubsequence(self, s: str) -> int:
        suf_cnt = [0] * 26
        for c in s[2:]:
            suf_cnt[ord(c) - ord('a')] += 1
        
        pre_cnt = [0] * 26
        pre_cnt[ord(s[0]) - ord('a')] += 1
        # print(pre_cnt, suf_cnt)
        ans = set()
        for i in range(1, len(s) - 1):
            od = ord(s[i]) - ord('a')
            for od2 in range(26):
                if pre_cnt[od2] > 0 and suf_cnt[od2] >0:
                    ans.add((od2, od, od2))
            pre_cnt[od] += 1
            suf_cnt[ord(s[i + 1]) - ord('a')] -= 1
        # print(ans)
        return len(ans) % (10 ** 9 + 7)

if __name__ == '__main__':
    s = Solution()
    print(s.countPalindromicSubsequence(s = "aabca"))