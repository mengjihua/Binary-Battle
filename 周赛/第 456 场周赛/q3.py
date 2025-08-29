from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 6 + 1)

class Solution:
    # 返回这 k 个子数组中 最大 XOR 的 最小值 。
    def minXor(self, nums: List[int], k: int) -> int:
        def check(x):
            cur_xor = 0
            for i in range(len(nums)):
                if cur_xor ^ nums[i] <= x:
                    cur_xor ^= nums[i]
                elif nums[i] <= x:
                    cur_xor = nums[i]
                else:
                    return False
            return True
        
        l, r = 0, max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                print(mid)
                r = mid - 1
            else:
                l = mid + 1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.minXor(nums = [1,2,3], k = 2))