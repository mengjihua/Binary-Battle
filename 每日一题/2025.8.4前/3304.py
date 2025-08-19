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
    # def kthCharacter(self, k: int) -> str:
    #     lst = [0]
    #     while len(lst) < k:
    #         temp = lst.copy()
    #         for i in range(len(lst)):
    #             temp.append((lst[i] + 1) % 26)
    #         # print(temp, lst)
    #         lst = temp
    #     return chr(lst[k - 1] + ord('a'))
    
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + bin(k - 1).count('1'))

# if __name__ == '__main__':
#     s = Solution()
#     print(s.kthCharacter(5))