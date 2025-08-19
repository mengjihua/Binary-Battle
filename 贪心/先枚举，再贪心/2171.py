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
    # 前面方法使用 Counter 是为了计算 pre_cnt
    def minimumRemoval(self, beans: List[int]) -> int:
        bean_cnt = Counter(beans)
        beans = sorted(bean_cnt.items(), key=lambda x: x[0])
        mx, n = beans[-1][0], sum(cnt for _, cnt in beans)
        # pre_cnt[i] 表示 1 到 i 的豆子数量
        pre_cnt = [0] * (mx + 1)
        p = 0
        for bean, cnt in beans:
            while p < bean:
                pre_cnt[p] = pre_cnt[p - 1]
                p += 1
            pre_cnt[bean] = pre_cnt[bean - 1] + cnt
            p += 1
        remain = -inf
        for i in range(1, mx + 1):
            remain = _max(remain, (n - pre_cnt[i - 1]) * i)
        return sum(bean * cnt for bean, cnt in beans) - remain
    
    # 离散化(仅保留有效前缀和) + 实时计算前缀和
    def minimumRemoval(self, beans: List[int]) -> int:
        bean_cnt = Counter(beans)
        beans = sorted(bean_cnt.items(), key=lambda x: x[0])
        sm, n = sum(bean * cnt for bean, cnt in beans), sum(cnt for _, cnt in beans)
        # pre_cnt[i] 表示 1 到 i 的豆子数量
        pre_cnt = remain = 0
        for bean, cnt in beans:
            remain = _max(remain, (n - pre_cnt) * bean)
            pre_cnt = pre_cnt + cnt
        return sm - remain
    
    # 无需Counter，直接排序
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        n = len(beans)
        return sum(beans) - max(beans[i] * (n - i) for i in range(n))
    
if __name__ == "__main__":
    s = Solution()
    # print(s.minimumRemoval([4, 1, 6, 5]))
    print(s.minimumRemoval([2, 10, 3, 2]))