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
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        num1_sum, num2_sum = sum(nums1), sum(nums2)
        num1_zero_count, num2_zero_count = nums1.count(0), nums2.count(0)
        num1_sum, num2_sum = num1_sum + num1_zero_count, num2_sum + num2_zero_count
        
        if num1_zero_count != 0 and num2_zero_count != 0:
            return max(num1_sum, num2_sum)
        elif num1_zero_count != 0:
            return max(num1_sum, num2_sum) if num1_sum <= num2_sum else -1
        elif num2_zero_count != 0:
            return max(num1_sum, num2_sum) if num2_sum <= num1_sum else -1
        else:
            return num1_sum if num1_sum == num2_sum else -1

if __name__ == "__main__":
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    solution = Solution()
    print(solution.minSum(nums1, nums2))  # Output: 15