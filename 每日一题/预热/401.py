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


def cal_min(turnedOn):
    res = []
    for i in range(60):
        if bin(i).count('1') == turnedOn:
            res.append(f'{i:02d}')
    return res

def cal_hour(turnedOn):
    res = []
    for i in range(12):
        if bin(i).count('1') == turnedOn:
            res.append(str(i))
    return res

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for m_turnedOn in range(turnedOn + 1):
            m = cal_min(m_turnedOn)
            h = cal_hour(turnedOn - m_turnedOn)
            for i in m:
                for j in h:
                    ans.append(j + ':' + i)
        return ans
    
    def readBinaryWatch1(self, turnedOn: int) -> List[str]:
        ans = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    ans.append(f"{h}:{m:02d}")
        return ans
    


# if __name__ == '__main__':
#     s = Solution()
#     start = timestamp()
#     turnedOn = int(input())
#     s.readBinaryWatch(turnedOn)
#     print('耗费时间: ', timestamp() - start)