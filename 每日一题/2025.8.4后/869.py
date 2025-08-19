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

# 打表, 写出所有2的幂的数字串
def print_2_power():
    power_of_2 = []
    for i in range(31):
        power_of_2.append(str(2 ** i))
    return power_of_2

# 相同长度的数字串计数后放入字典
def group_by_length(power_of_2):
    grouped = defaultdict(list)
    for num in power_of_2:
        grouped[len(num)].append(Counter(num))
    return grouped
    
group = group_by_length(print_2_power())
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        return Counter(str(n)) in group[len(str(n))]