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


class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        n = len(value)
        val_lim_zip = sorted(zip(value, limit), key=lambda x: (x[1], -x[0]))
        val = [vl[1] for vl in val_lim_zip]
        
        ans = 0
        cnt = 0
        invalid = [False] * n
        i = 0
        temp = -1
        while i < n:
            if invalid[i]:
                i += 1
                continue
                
            if cnt < val_lim_zip[i][1]:
                ans += val_lim_zip[i][0]
                cnt += 1
                
                # TODO: 重点, 二分, 这里不能从range(i + 1, n)开始, 因为还要考虑到之前的元素
                idx = bisect_right(val, cnt) - 1
                
                if idx >= temp:
                    for k in range(temp + 1, idx + 1):
                        if not invalid[k]:
                            invalid[k] = True
                            if k <= i:
                                cnt -= 1
                    temp = idx
            i = _max(temp + 1, i + 1)
                
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.maxTotal(value = [83967,28721,97877], limit = [2,1,2]))
    print(s.maxTotal(value = [4,2,6], limit = [1,1,1]))