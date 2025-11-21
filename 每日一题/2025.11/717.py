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
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        last_bit = None
        for b in bits[:-1]:
            if b == 1 and last_bit is None:
                # 上一个字符已经用掉, 但是当前是 1, 无法单独组成比特
                last_bit = 1
            else:
                # 无论是 b == 0, 还是 last_bit != None, 都说明可以组合一个比特
                last_bit = None
        return last_bit is None

if __name__ == "__main__":
    s = Solution()
    print(s.isOneBitCharacter(bits = [1,1,1,0]))
    print(s.isOneBitCharacter(bits = [1,1,0,0]))