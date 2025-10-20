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
    def lexGreaterPermutation(self, s: str, target: str) -> str:
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

    def lexGreaterPermutation(self, s: str, target: str) -> str:
        def f(count, suf):
            cnt = count.copy()
            for i in range(len(suf)):
                idx = ord(suf[i]) - ord('a')
                for j in range(idx + 1, 26):
                    if cnt[j] > 0:
                        return True
                if cnt[idx] == 0:
                    return False
                cnt[idx] -= 1
            return False
        
        n = len(s)
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        res = []
        for i in range(n):
            idx = ord(target[i]) - ord('a')
            judge = False
            for c in range(26):
                if count[c] == 0:
                    continue
                cc = chr(c + ord('a'))
                if c > idx:
                    res.append(cc)
                    count[c] -= 1
                    for j in range(26):
                        if count[j] > 0:
                            res.append(chr(j + ord('a')) * count[j])
                    return ''.join(res)
                elif c == idx:
                    count[c] -= 1
                    if f(count, target[i + 1:]):
                        res.append(cc)
                        judge = True
                        break
                    else:
                        count[c] += 1
            if not judge:
                return ""
        return ""
    
if __name__ == "__main__":
    s = Solution()
    print(s.lexGreaterPermutation(s = "bb", target = "ba"))