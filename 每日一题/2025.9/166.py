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
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return str(0)

        sign = '-' if (numerator < 0) ^ (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        
        # 计算整数部分
        int_part, remainder = divmod(numerator, denominator)
        if remainder == 0:
            return f"{sign}{int_part}"
        
        # 计算小数部分
        suf_digits = []  # 小数数位
        remainder_pos = {} # 余数出现的位置
        while remainder != 0 and remainder not in remainder_pos:
            remainder_pos[remainder] = len(suf_digits)
            remainder *= 10
            digit = remainder // denominator
            suf_digits.append(str(digit))
            remainder = remainder % denominator
            
        if remainder != 0:
            # 有循环节
            loop_start = remainder_pos[remainder]
            no_loop = ''.join(suf_digits[:loop_start])
            loop = ''.join(suf_digits[loop_start:])
            return f"{sign}{int_part}.{no_loop}({loop})"
        else:
            return f"{sign}{int_part}." + ''.join(suf_digits)


if __name__ == "__main__":
    s = Solution()
    print(s.fractionToDecimal(numerator = 4, denominator = 333))
    print(s.fractionToDecimal(1, 214748364))