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
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        temp = [0] * 101
        ans = []
        for i in range(n):
            temp[nums[i] + 50] += 1
            if i < k - 1:
                continue
            tt = x
            for j in range(101):
                if temp[j] > 0:
                    # print(i + 1, j - 50, temp[j], tt)
                    tt -= temp[j]
                if tt <= 0:
                    ans.append(j - 50 if j - 50 < 0 else 0)
                    break

            temp[nums[i - k + 1] + 50] -= 1
            # print('----------------------------------------')
        return ans


if __name__ == '__main__':
    s = Solution()
    # print(s.getSubarrayBeauty(nums=[1, -1, -3, -2, 3], k=3, x=2))
    print(s.getSubarrayBeauty([-3, 1, 2, -3, 0, -3], 2, 1))
    # print(log(10 ** 5, 2))