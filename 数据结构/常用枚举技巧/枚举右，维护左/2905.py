from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class SimpleSortedList:
    def __init__(self):
        """初始化有序列表"""
        self.data = []

    def add(self, value):
        """将值插入到有序列表中"""
        index = bisect_right(self.data, value)
        self.data.insert(index, value)

    def __getitem__(self, index):
        """返回指定索引的元素"""
        return self.data[index]

    def __len__(self):
        """返回列表长度"""
        return len(self.data)

    def __repr__(self):
        """描述对象"""
        return f"SimpleSortedList({self.data})"
    

class Solution:
    # def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
    #     n = len(nums)
    #     if n <= indexDifference:
    #         return [-1, -1]

    #     pre_min, pre_max = [[0, 0] for _ in range(n)], [[0, 0] for _ in range(n)]
    #     pre_min[0] = pre_max[0] = (0, nums[0])
    #     for i in range(1, n):
    #         if nums[i] < pre_min[i - 1][1]:
    #             pre_min[i] = (i, nums[i])
    #         else:
    #             pre_min[i] = pre_min[i - 1]
    #         if nums[i] > pre_max[i - 1][1]:
    #             pre_max[i] = (i, nums[i])
    #         else:
    #             pre_max[i] = pre_max[i - 1]

    #     suf_min, suf_max = [[0, 0] for _ in range(n)], [[0, 0] for _ in range(n)]
    #     suf_min[-1] = suf_max[-1] = (n - 1, nums[-1])
    #     for i in range(n - 2, -1, -1):
    #         if nums[i] < suf_min[i + 1][1]:
    #             suf_min[i] = (i, nums[i])
    #         else:
    #             suf_min[i] = suf_min[i + 1]
    #         if nums[i] > suf_max[i + 1][1]:
    #             suf_max[i] = (i, nums[i])
    #         else:
    #             suf_max[i] = suf_max[i + 1]

    #     for l in range(n):
    #         r = l + indexDifference
    #         if r >= n:
    #             break
    #         # print(l, r, pre_min[l], suf_max[r], pre_max[l], suf_min[r])
    #         if abs(pre_min[l][1] - suf_max[r][1]) >= valueDifference:
    #             return [pre_min[l][0], suf_max[r][0]]
    #         if abs(pre_max[l][1] - suf_min[r][1]) >= valueDifference:
    #             return [pre_max[l][0], suf_min[r][0]]
    #     return [-1, -1]

    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mx, mn = -inf, inf
        l1, l2 = -1, -1
        for l, num in enumerate(nums[indexDifference:]):
            if nums[l] > mx:
                mx = nums[l]
                l1 = l
            if nums[l] < mn:
                mn = nums[l]
                l2 = l

            if abs(mx - num) >= valueDifference:
                return [l1, l + indexDifference]
            if abs(mn - num) >= valueDifference:
                return [l2, l + indexDifference]
        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    print(s.findIndices(nums=[5, 1, 4, 1], indexDifference=2, valueDifference=4))
    start = timestamp()
    print(s.findIndices([5,1,4,1] * (2 * 10 ** 4 + 1), 2, 4))
    end = timestamp()
    print(f"耗时: {(end - start):.2f}秒")