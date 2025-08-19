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
    # def continuousSubarrays(self, nums: List[int]) -> int:
        # ans, l = 0, 0
        # window = defaultdict(int)
        # for r in range(len(nums)):
        #     window[nums[r]] += 1
        #     while max(window) - min(window) > 2:
        #         window[nums[l]] -= 1
        #         if window[nums[l]] == 0:
        #             del window[nums[l]]
        #         l += 1
        #     ans += r - l + 1
        #     # print(f"l: {l}, r: {r}, ans: {ans}, window: {window}, added: {r - l + 1}")
        # return ans

    def continuousSubarrays(self, nums: List[int]) -> int:
        min_q, max_q = deque(), deque()
        ans, l = 0, 0
        for r in range(len(nums)):
            while min_q and nums[r] <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(r)
            while max_q and nums[r] >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(r)
            
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                l += 1
                if min_q[0] < l:
                    min_q.popleft()
                if max_q[0] < l:
                    max_q.popleft()
            ans += r - l + 1
        return ans

# if __name__ == '__main__':
#     s = Solution()
#     print(s.continuousSubarrays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#     print(s.continuousSubarrays(nums = [5,4,2,4]))
#     print(s.continuousSubarrays(nums = [1,2,3]))