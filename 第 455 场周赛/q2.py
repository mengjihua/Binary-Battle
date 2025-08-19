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
    # def findCoins(self, numWays: List[int]) -> List[int]:
    #     ans = []
    #     n = len(numWays)

    #     # 求 ans 的元素组成 i 的方法数
    #     def calculateCounts(depth, i):
    #         if i == 0:
    #             return 1
    #         if depth == le:
    #             return 0

    #         res = 0
    #         num = ans[depth]
    #         for cnt in range(floor(i / num), -1, -1):
    #             res += calculateCounts(depth + 1, i - cnt * num)
    #         return res

    #     for i in range(n):
    #         if numWays[i] == 0:
    #             continue

    #         if not ans and numWays[i] == 1:
    #             ans.append(i + 1)
    #             continue

    #         le = len(ans)
    #         cnt = calculateCounts(0, i + 1)
    #         if cnt == numWays[i]:
    #             continue
    #         elif cnt == numWays[i] - 1:
    #             ans.append(i + 1)
    #         else:
    #             return []

    #     return ans

    def findCoins(self, numWays: List[int]) -> List[int]:
        n = len(numWays)
        full_dp = [0] * (n + 1)
        full_dp[0] = 1
        for i in range(1, n + 1):
            full_dp[i] = numWays[i - 1]
        
        current_dp = [0] * (n + 1)
        current_dp[0] = 1
        S = []
        
        for i in range(1, n + 1):
            F_i = current_dp[i]
            diff = full_dp[i] - F_i
            if diff == 1:
                S.append(i)
                for j in range(i, n + 1):
                    current_dp[j] += current_dp[j - i]
            elif diff != 0:
                return []
        return S


if __name__ == '__main__':
    s = Solution()
    # print(s.findCoins([1, 2, 3, 4, 5]))
    print(s.findCoins([0, 1, 0, 2, 0, 3, 0, 4, 0, 5]))
    print(s.findCoins([1, 2, 2, 3, 4]))
    print(s.findCoins([0, 0, 0, 0, 0]))
    print(s.findCoins([1, 0]))
