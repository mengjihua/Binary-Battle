from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    def countSatisfyingPairs(self, nums: List[int], indexDifference: int, valueDifference: int) -> int:
        n = len(nums)
        # 特殊情况判定, 从中有序挑选两个元素, 包括本身(i, i)
        if indexDifference == 0 and valueDifference == 0:
            return n * (n - 1) + n
        
        count = 0
        # 维护一个滑动窗口中的 nums[l] 的有序数组，l <= r - indexDifference
        sl = SortedList()
        
        for r in range(n):
            # 当前 r，可以加入满足 l <= r - indexDifference 的 nums[l] 到有序数组中
            if r >= indexDifference:
                sl.add(nums[r - indexDifference])

            # 现在，sl 是所有满足 l <= r - indexDifference 的 nums[l]
            # 找出其中有几个满足 abs(nums[r] - nums[l]) >= valueDifference
            if sl:
                # nums[r] - nums[l] >= valueDifference -> nums[l] <= nums[r] - valueDifference
                left = bisect_right(sl, nums[r] - valueDifference)
                # nums[l] - nums[r] >= valueDifference -> nums[l] >= nums[r] + valueDifference
                right = len(sl) - bisect_left(sl, nums[r] + valueDifference)
                # print(f"r: {r}, left: {left}, right: {right}, sl: {sl}")
                count += (left + right) * 2

        return count

    
if __name__ == '__main__':
    s = Solution()
    print(s.countSatisfyingPairs(nums = [2,1], indexDifference = 0, valueDifference = 0))
    print(s.countSatisfyingPairs(nums = [5,1,4,1], indexDifference = 2, valueDifference = 4))
    start = timestamp()
    print(s.countSatisfyingPairs([5,1,4,1] * (2 * 10 ** 4 + 1), 2, 4))
    end = timestamp()
    print(f"耗时: {(end - start):.2f}秒")