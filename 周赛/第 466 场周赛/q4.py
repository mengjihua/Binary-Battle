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
    def countBinaryPalindromes(self, n: int) -> int:
        # 如果 n 为 0，只有一个回文数 0
        if n == 0:
            return 1

        mx_l = len(bin(n)) - 2  # n 的二进制长度
        ans = 1  # 包含 0

        # 枚举长度小于 mx_l 的所有二进制回文数
        for l in range(1, mx_l):
            half_len = ceil(l / 2)  # 回文数的一半长度
            ans += (1 << (half_len - 1))  # 该长度的回文数个数

        half_len = ceil(mx_l / 2)
        mn = 1 << (half_len - 1)  # 最小的半部分
        pre = int(bin(n)[2:][:half_len], 2)  # n 的前半部分
        ans += (pre - mn)  # 加上前半部分在范围内的回文数

        s = bin(pre)[2:]  # 前半部分的二进制字符串
        # 拼接成回文串
        if mx_l % 2 == 0:
            temp = s + s[::-1]
        else:
            temp = s + s[:-1][::-1]

        # 判断拼接后的回文数是否小于等于 n
        return ans + 1 if int(temp, 2) <= n else ans


# print(log(10 ** 15, 2))