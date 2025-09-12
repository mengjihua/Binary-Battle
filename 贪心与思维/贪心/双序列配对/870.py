from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

class Solution:
    # def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     nums1_map = sorted((num, idx) for idx, num in enumerate(nums1))
    #     nums2_map = sorted((num, idx) for idx, num in enumerate(nums2)) 
        
    #     temp1 = [-1] * len(nums1)
    #     temp2 = []
    #     idx1, n = 0, len(nums1)
    #     for num2, idx2 in nums2_map:
    #         while idx1 < n and nums1_map[idx1][0] <= num2:
    #             temp2.append(nums1_map[idx1][0])
    #             idx1 += 1
    #         if idx1 >= n:
    #             break
    #         temp1[idx2] = nums1_map[idx1][0]
    #         idx1 += 1
        
    #     ans = []
    #     for i in range(len(nums1)):
    #         if temp1[i] != -1:
    #             ans.append(temp1[i])
    #         else:
    #             ans.append(temp2.pop())
    #     return ans
    
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        
        n = len(nums1)
        idxs = sorted(range(n), key=lambda i: nums2[i])
        
        ans = [-1] * n
        l, r = 0, n - 1
        for num in nums1:
            if num > nums2[idxs[l]]:
                ans[idxs[l]] = num
                l += 1
            else:
                ans[idxs[r]] = num
                r -= 1
        return ans
    

if __name__ == '__main__':
    s = Solution()
    print(s.advantageCount(nums1 = [2,7,11,15], nums2 = [1,10,4,11]))  # Output: [2,11,7,15]
    print(s.advantageCount(nums1 = [12,24,8,32], nums2 = [13,25,32,11]))  # Output: [24,32,8,12]