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
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     temp, idx = float('inf'), -1
    #     for i in range(len(arr)):
    #         if abs(arr[i] - x) < temp:
    #             idx = i
    #             temp = abs(arr[i] - x)
                
    #     ans = [arr[idx]]
    #     l, r, k = idx - 1, idx + 1, k - 1
    #     while l >= 0 and r < len(arr) and k > 0:
    #         if abs(arr[l] - x) <= abs(arr[r] - x):
    #             ans.append(arr[l])
    #             l -= 1
    #         else:
    #             ans.append(arr[r])
    #             r += 1
    #         k -= 1
    #     while l >= 0 and k > 0:
    #         ans.append(arr[l])
    #         l -= 1
    #         k -= 1
    #     while r < len(arr) and k > 0:
    #         ans.append(arr[r])
    #         r += 1
    #         k -= 1
    #     # print(ans)
    #     return sorted(ans)
    
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     l, r = 0, len(arr) - 1
    #     while r - l + 1 > k:
    #         if abs(arr[l] - x) <= abs(arr[r] - x):
    #             r -= 1
    #         else:
    #             l += 1
    #     return arr[l:r + 1]
    
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k - 1
        while l <= r:
            mid = (l + r) // 2
            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid - 1
        return arr[l:l + k]

if __name__ == '__main__':
    s = Solution()
    print(s.findClosestElements([1,2,3,4,5], 4, 3))