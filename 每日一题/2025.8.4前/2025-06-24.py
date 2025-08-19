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
    # def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
    #     target_idx = []
    #     for i, num in enumerate(nums):
    #         if num == key:
    #             target_idx.append(i)
        
    #     ans = []
    #     for i in range(len(nums)):
    #         for j in target_idx:
    #             if abs(i - j) <= k:
    #                 ans.append(i)
    #                 break
    #     return ans
    
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        target_idx = []
        for i, num in enumerate(nums):
            if num == key:
                target_idx.append(i)
                
        ans, idx, start = [], 0, max(0, target_idx[0] - k)
        for i in range(start, len(nums)):
            if idx >= len(target_idx):
                break
            if abs(target_idx[idx] - i) <= k:
                ans.append(i)
            elif target_idx[idx] - i > k:
                continue
            else:
                idx += 1
                if idx < len(target_idx) and target_idx[idx] - i <= k:
                    ans.append(i)
        return ans

if __name__ == '__main__':
    s = Solution()
    # nums = [1,2,3,4,5]
    # key = 5
    # k = 2
    # print(s.findKDistantIndices(nums, key, k))
    nums = [3,4,9,1,3,9,5]
    key = 9
    k = 1
    print(s.findKDistantIndices(nums, key, k))
    nums = [1,2,2,2,2,1]
    key, k = 1, 1
    print(s.findKDistantIndices(nums, key, k))