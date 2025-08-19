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
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = bisect_left(fruits, [startPos - k])  # 向左最远能到 fruits[left][0]
        right = bisect_left(fruits, [startPos + 1])  # 位置 <= startPos 的最大下标 + 1
        ans = temp = sum(f[1] for f in fruits[left: right])  # 从 fruits[left][0] 到 startPos 的水果数
        # 枚举最右走到 fruits[right][0]
        while right < len(fruits) and fruits[right][0] <= startPos + k:
            temp += fruits[right][1]
            while fruits[right][0] * 2 - fruits[left][0] - startPos > k and \
                  fruits[right][0] - fruits[left][0] * 2 + startPos > k:
                temp -= fruits[left][1]  # fruits[left][0] 太远了
                left += 1
            ans = max(ans, temp)  # 更新答案最大值
            right += 1  # 继续枚举下一个最右位置
        return ans