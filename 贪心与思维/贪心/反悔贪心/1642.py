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

# TODO 发题解
class Solution:
    # 反悔堆, 先用砖块填平(进堆), 
    # 然后如果砖块不够了, 就用梯子填平, 然后把梯子填平的差值换回砖块(取高度最大值 -> 出堆)
    # # 如果砖块和梯子都不够了, 就返回当前的高度
    # 这种方法的时间复杂度是 O(n log n)，其中 n 是建筑物的数量。
    # 空间复杂度是 O(n)，用于存储堆.
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap, n = [], len(heights)
        for i in range(n - 1):
            if heights[i] >= heights[i + 1]:
                continue
            need = heights[i + 1] - heights[i]
            heappush(heap, -need)
            if bricks >= need:
                bricks -= need
            else:
                while heap and ladders > 0 and bricks < need:
                    ladders -= 1
                    bricks -= heappop(heap)
                if bricks < need:
                    return i
                bricks -= need
        return n - 1

if __name__ == '__main__':
    s = Solution()
    print(s.furthestBuilding(heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
    print(s.furthestBuilding(heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
    print(s.furthestBuilding(heights=[1, 5, 1, 2, 3, 4, 10000], bricks=4, ladders=1))
