from typing import List
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    #     ans, l1, l2, cur_sum1, cur_sum2 = 0, 0, 0, 0, 0
    #     for r, num in enumerate(nums):
    #         cur_sum1 += num
    #         cur_sum2 += num
            
    #         while l1 <= r and cur_sum1 > goal:
    #             cur_sum1 -= nums[l1]
    #             l1 += 1
    #         while l2 <= r and cur_sum2 >= goal:
    #             cur_sum2 -= nums[l2]
    #             l2 += 1
            
    #         if cur_sum1 + cur_sum2 >= goal:
    #             ans += l2 - l1
    #     return ans
    
    
    # def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    #     ans1, l1, cur_sum1 = 0, 0, 0
    #     for r,  num in enumerate(nums):
    #         cur_sum1 += num
    #         while l1 <= r and cur_sum1 > goal:
    #             cur_sum1 -= nums[l1]
    #             l1 += 1
    #         ans1 += r - l1 + 1
        
    #     ans2, l2, cur_sum2 = 0, 0, 0
    #     for r, num in enumerate(nums):
    #         cur_sum2 += num
    #         while l2 <= r and cur_sum2 >= goal:
    #             cur_sum2 -= nums[l2]
    #             l2 += 1
    #         ans2 += r - l2 + 1
    #     return ans1 - ans2
    
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans, r1, r2, cur_sum1, cur_sum2, n = 0, 0, 0, 0, 0, len(nums)
        for l in range(n):
            while r1 < n and cur_sum1 < goal:
                cur_sum1 += nums[r1]
                r1 += 1
            while r2 < n and cur_sum2 <= goal:
                cur_sum2 += nums[r2]
                r2 += 1
            if cur_sum1 >= goal:
                if r1 <= l:
                    ans += n - l
                else:
                    ans += n - r1 + 1
            if cur_sum2 > goal:
                ans -= n - r2 + 1
            # print(f'l :{l}, r1 :{r1}, r2 :{r2}, cur_sum1 :{cur_sum1}, cur_sum2 :{cur_sum2}, ans :{ans}')
            cur_sum1, cur_sum2 = cur_sum1 - nums[l], cur_sum2 - nums[l]
        return ans
    
    
# if __name__ == '__main__':
#     s = Solution()
#     print(s.numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))
#     print(s.numSubarraysWithSum(nums = [0,0,0,0,0], goal = 0))