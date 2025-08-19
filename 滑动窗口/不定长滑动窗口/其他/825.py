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
    def numFriendRequests(self, ages: List[int]) -> int:
        count = Counter(ages)
        # 使得nums[r] >= nums[l]
        cntItem_lst = sorted(count.items())
        # 计算相同年龄的人发出的请求
        # base_ans = 0
        # for age, c in cntItem_lst:
        #     # ages[l] <= 0.5 * ages[r] + 7 => ages[r] <= 14
        #     if age <= 14:
        #         continue
        #     base_ans += c * (c - 1)
        # => 直接在下面更新

        ans, l = 0, 0
        length = 0
        for r, (age, cnt) in enumerate(cntItem_lst):
            while l < r and cntItem_lst[l][0] <= 0.5 * age + 7:
                length -= cntItem_lst[l][1]
                l += 1
            ans += length * cnt + (cnt * (cnt - 1) if age > 14 else 0)
            length += cnt
        return ans

# if __name__ == "__main__":
#     s = Solution()
#     print(s.numFriendRequests([16,16]))
#     print(s.numFriendRequests([16,17,18]))
#     print(s.numFriendRequests([20,30,100,110,120]))
