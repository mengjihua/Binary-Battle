from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
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
    def maxProduct(self, nums: List[int]) -> int:
        w = max(nums).bit_length()
        u = 1 << w
        f = [0] * u  # f[s] 表示能由 s 的子集构成的原始数的最大值
        for x in nums:
            f[x] = x  # 初始值

        for s in range(u):  # 从小到大枚举集合 s
            for i in range(w):  # 枚举 s 中的元素 i
                if s >> i & 1:  # i 属于集合 s
                    v = f[s ^ (1 << i)]  # 从 s 的子集 s \ {i} 转移过来
                    if v > f[s]:
                        f[s] = v  # 手写 max 更快

        return max(x * f[(u - 1) ^ x] for x in nums)
    

# print((1 << 20) * 20) # 20971520