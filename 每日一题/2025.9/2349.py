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
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.index_to_num = defaultdict(int)
        self.num_to_indices = defaultdict(SortedList)

    def change(self, index: int, number: int) -> None:
        # 如果 index 已经存在旧的 number，先移除旧的映射
        old_num = self.index_to_num[index]
        if old_num != 0:
            self.num_to_indices[old_num].remove(index)
        # 将新的映射加入
        self.index_to_num[index] = number
        self.num_to_indices[number].add(index)

    def find(self, number: int) -> int:
        # 查找 number 对应的最小 index, 如果不存在返回 -1
        indices = self.num_to_indices[number]
        return indices[0] if indices else -1

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)