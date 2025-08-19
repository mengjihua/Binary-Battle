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
    # def countKConstraintSubstrings(self, s: str, k: int) -> int:
    #     ans , l = 0, 0
    #     window = [0] * 2
    #     for r in range(len(s)):
    #         window[int(s[r])] += 1
    #         while window[0] > k and window[1] > k:
    #             window[int(s[l])] -= 1
    #             l += 1
    #         ans += r - l + 1
    #         # print(f"l: {l}, r: {r}, ans: {ans}, window: {window}, added: {r - l + 1}")
    #     return ans
    
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        limit_cnt = 2
        ans , l, cur_cnt = 0, 0, 0
        window = defaultdict(int)
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == k + 1:
                cur_cnt += 1
            while cur_cnt >= limit_cnt:
                window[s[l]] -= 1
                if window[s[l]] == k:
                    cur_cnt -= 1
                l += 1
            ans += r - l + 1
            # print(f"l: {l}, r: {r}, ans: {ans}, window: {window}, added: {r - l + 1}, cur_cnt: {cur_cnt}")
        return ans

# if __name__ == '__main__':
#     s = "10101"
#     k = 1
#     print(Solution().countKConstraintSubstrings(s, k))
#     s = "11111"
#     k = 1
#     print(Solution().countKConstraintSubstrings(s, k))