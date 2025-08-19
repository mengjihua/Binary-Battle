from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)

# TODO 发题解
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n, m = len(houses), len(heaters)

        def check(radius):
            # 定义一个列表 heat_range，用于存储每个加热段的加热范围
            heat_range = []
            # 遍历 heaters
            for i in range(m):
                # 计算每个 heater 的加热范围
                l, r = heaters[i] - radius, heaters[i] + radius
                # 如果 heat_range 不为空，并且当前 heater 的加热范围与上一个 heater 的加热范围有重叠，则合并加热范围
                if heat_range and heat_range[-1][1] >= l:
                    heat_range[-1][1] = max(heat_range[-1][1], r)
                # 否则，将当前 heater 的加热范围添加到 heat_range 中
                else:
                    heat_range.append([l, r])

            # 定义两个指针 p 和 limit，用于遍历 houses 和 heat_range
            p, limit = 0, len(heat_range)
            # 遍历 houses
            for i in range(n):
                # 如果当前 house 不在任何 heater 的加热范围内，则返回 False
                while p < limit and houses[i] > heat_range[p][1]:
                    p += 1
                if p == limit or houses[i] < heat_range[p][0]:
                    return False

            # 如果所有 house 都在 heater 的加热范围内，则返回 True
            return True

        # 二分查找
        l, r = 0, max(abs(houses[-1] - heaters[m // 2]), abs(heaters[m // 2] - houses[0]))
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        max_radius = 0

        for house in houses:
            # 二分查找，找到应放置该房屋的位置
            left = bisect_left(heaters, house)

            # left 是插入点，比较与前后供暖器的距离
            min_dist = float('inf')
            # 如果插入点在供暖器列表中，则比较与该供暖器的距离
            if left < len(heaters):
                min_dist = abs(heaters[left] - house)
            # 如果插入点有前一个点位在供暖器列表中，则比较与前一个供暖器的距离
            if left > 0:
                min_dist = min(min_dist, abs(heaters[left - 1] - house))

            # 更新最大半径
            max_radius = max(max_radius, min_dist)

        return max_radius

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        p = 0  # 指针指向 heaters
        max_radius = 0
        n = len(heaters)

        for house in houses:
            # 移动 i 找到离 house 最近的 heater
            while p < n and heaters[p] < house:
                p += 1

            # 离 house 最近的 heater 是 heaters[i] 或 heaters[i-1]
            left_dist = float('inf') if p == 0 else abs(heaters[p - 1] - house)
            right_dist = float('inf') if p == n else abs(heaters[p] - house)

            min_dist = min(left_dist, right_dist)
            max_radius = max(max_radius, min_dist)

        return max_radius
