from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def maximumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s = sum(cards[:cnt])  # 最大的 cnt 个数之和
        if s % 2 == 0:  # s 是偶数
            return s

        def replaced_sum(x: int) -> int:
            for v in cards[cnt:]:
                if v % 2 != x % 2:  # 找到一个最大的奇偶性和 x 不同的数
                    return s - x + v  # 用 v 替换 s
            return 0

        x = cards[cnt - 1]
        ans = replaced_sum(x)  # 替换 x
        for v in cards[cnt - 1::-1]:
            if v % 2 != x % 2:  # 找到一个最小的奇偶性和 x 不同的数
                ans = max(ans, replaced_sum(v))  # 替换
                break
        return ans