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

# TODO 发题解
class Solution:
    # 1. 先建立一个高度差的 diff。
    # 2. 对于每次循环，得到前 mid 个高度差并进行排序, 去除前ladder个（用梯子）， 
    # 3. 将剩余的高度差求和 与 砖块数比较。
    # 4. 如果和小于等于砖块数，则说明可以到达 mid 个建筑物，继续向右查找。
    # 5. 如果和大于砖块数，则说明不能到达 mid 个建筑物，向左查找。
    # 这种方法的时间复杂度是 O(n log n log n)，其中 n 是建筑物的数量。
    # 空间复杂度是 O(n)，用于存储高度差。
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n, diff = len(heights), []
        for i in range(n - 1):
            diff.append(heights[i + 1] - heights[i])
            
        def check(h):
            cur_diff = [i for i in diff[:h] if i > 0]
            cur_diff.sort(reverse=True)
            return sum(cur_diff[ladders:]) <= bricks
        
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                l = mid + 1
            else:
                r = mid - 1
        return r

if __name__ == '__main__':
    s = Solution()
    print(s.furthestBuilding(
        heights=[4, 2, 7, 6, 9, 14, 12], bricks=5, ladders=1))
    print(s.furthestBuilding(
        heights=[4, 12, 2, 7, 3, 18, 20, 3, 19], bricks=10, ladders=2))
    print(s.furthestBuilding(
        heights=[1, 5, 1, 2, 3, 4, 10000], bricks=4, ladders=1))
