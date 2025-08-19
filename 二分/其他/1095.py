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

# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
class MountainArray:
    def __init__(self, arr: List[int]):
        self.arr = arr
    
    def get(self, index: int) -> int:
        return self.arr[index]
   
    def length(self) -> int:
        return len(self.arr)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n, temp_idx = mountainArr.length(), 1
        if n < 3:
            return -1
        
        # 找到最高峰索引
        def query_peak(x):
            q_num = mountainArr.get(x + 1)
            num = mountainArr.get(x)
            if q_num < num:
                return -1
            else:
                return 1
        l, r = 1, n - 2
        while l <= r:
            mid = (l + r) // 2
            if query_peak(mid) == 1:
                l = mid + 1
            else:
                r = mid - 1
        temp_idx = r + 1
        if mountainArr.get(temp_idx) == target:
            return temp_idx
        
        def check(index):
            num = mountainArr.get(index)
            if num == target:
                return 0
            elif num < target:
                return 1
            return -1
        
        # 左边山峰寻找 target
        l, r = 0, temp_idx - 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid) == 0:
                return mid
            elif check(mid) == 1:
                l = mid + 1
            else:
                r = mid - 1
        
        # 右边山峰寻找 target
        l, r = temp_idx + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            if check(mid) == 0:
                return mid
            elif check(mid) == 1:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1

if __name__ == "__main__":
    s = Solution()
    mountainArr = MountainArray([1,2,3,4,5,3,1])
    print(s.findInMountainArray(target = 3, mountainArr=mountainArr))
    mountainArr = MountainArray([1,5,2])
    print(s.findInMountainArray(target = 2, mountainArr=mountainArr))
    mountainArr = MountainArray([1,2,5,1])
    print(s.findInMountainArray(target = 5, mountainArr=mountainArr))