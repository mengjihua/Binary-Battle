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
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        pre = [-1] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                pre[i] = st[-1]
            st.append(i)
        
        suf = [-1] * n
        st = []
        for i in range(n - 1, -1, -1):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                suf[i] = st[-1]
            st.append(i)
        
        ans = 0
        for i in range(n):
            if pre[i] != -1 and i - pre[i] > 1:
                ans += 1
            if suf[i] != -1 and suf[i] - i > 1:
                ans += 1
        return ans