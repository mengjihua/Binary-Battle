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
MOD = 10 ** 9 + 7

class Solution:
    def maximum69Number1 (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
    
    def maximum69Number2 (self, num: int) -> int:
        max_base = 0
        base = 1
        x = num
        while x:
            x, d = divmod(x, 10)
            if d == 6:
                max_base =  base
            base *= 10
        return num + max_base * 3

# 测试两者的性能差异
def test_performance():
    import timeit
    test_num = int(str(9) * 2000 + str(6) * 2000 + str(9) * 200)
    time1 = timeit.timeit(lambda: Solution().maximum69Number1(test_num), number=1000)
    time2 = timeit.timeit(lambda: Solution().maximum69Number2(test_num), number=1000)
    print(f"Time for method 1: {time1}")
    print(f"Time for method 2: {time2}")

if __name__ == "__main__":
    test_performance()