from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify
import sys
sys.setrecursionlimit(10 ** 5 + 1)


class SumOfFirstNTerms:
    # 已知首项和等差以及前n项和的最大值, 求前n项的最大个数
    def max_terms(self, a1: int, d: int, s_max: int) -> int:
        '''
            a1: 首项
            d: 等差
            s_max: 前n项和的最大值
        '''
        # 特殊情况处理
        if d == 0:
            if a1 == 0:
                return float('inf')  # 所有项都是0，可以无限取
            elif a1 > 0:
                return 0  # 所有项都大于0，无法取任何项使总和<=0
            else:
                return s_max // abs(a1)  # 每一项都是负数，尽可能多取

        # 求解二次方程的根
        a = d
        b = 2 * a1 - d
        c = -2 * s_max

        discriminant = b * b - 4 * a * c
        if discriminant < 0:
            return 0

        sqrt_d = sqrt(discriminant)
        n1 = (-b + sqrt_d) / (2 * a)
        n2 = (-b - sqrt_d) / (2 * a)

        # 只取正根
        n = int(max(n1, n2))

        # 验证是否满足条件
        while n >= 0:
            if n / 2 * (2 * a1 + (n - 1) * d) <= s_max:
                return n
            n -= 1
        return 0

    # 已知首项, 等差, n项, 求前n项和
    def sum_of_first_n_terms(self, a1: int, d: int, n: int) -> int:
        '''
            a1: 首项
            d: 等差
            n: 前n项的个数
        '''
        return n * (2 * a1 + (n - 1) * d) // 2


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        ns = SumOfFirstNTerms()

        def check(x):
            pre_len, suf_len = index, n - index - 1
            l_min_num, r_min_num = x - pre_len * 1, x - suf_len * 1

            def calc_sum(min_num, length):
                if min_num >= 1:
                    return ns.sum_of_first_n_terms(x - 1, -1, length)
                else:
                    m = length - 1 + min_num
                return ns.sum_of_first_n_terms(1, 1, m) + 1 - min_num

            pre_sum, suf_sum = calc_sum(l_min_num, pre_len), calc_sum(r_min_num, suf_len)

            return pre_sum + suf_sum + x <= maxSum

        l, r = 1, maxSum - (n - 1)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r


if __name__ == '__main__':
    s = Solution()
    # print(s.maxValue(n=4, index=2, maxSum=6))
    # print(s.maxValue(n=6, index=1, maxSum=10))
    print(s.maxValue(4, 0, 4))
