from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sys import setrecursionlimit, stdin, stdout
setrecursionlimit(5 * 10 ** 5 + 1)
input = lambda: stdin.readline().rstrip()
def _max(a, b): return a if a > b else b
def _min(a, b): return a if a < b else b
MOD = 10 ** 9 + 7

class XorBasis:
    def __init__(self, n: int):
        """ 初始化一个大小为 n 的线性基 """
        self.b = [0] * n

    def insert(self, x: int) -> None:
        ''' 
            向线性基中插入一个数 x
            若 x 能被已有基表示，则不插入（线性相关）
            否则插入 x (线性无关)
        '''
        b = self.b
        for i in range(len(b) - 1, -1, -1):
            if x >> i:
                if b[i] == 0:
                    b[i] = x
                    return True
                x ^= b[i]
        return False

    def max_xor(self) -> int:
        ''' 返回线性基能表示的最大异或和 '''
        b = self.b
        res = 0
        for i in range(len(b) - 1, -1, -1):
            res = _max(res, res ^ b[i])
        return res


class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        mx_bit_len = len(bin(max(nums))[2:])
        
        u = 1 << n
        sub_and = [0] * u
        sub_xor = [0] * u
        sub_and[0] = -1
        for i, num in enumerate(nums):
            hi_bit = 1 << i
            for mask in range(hi_bit):
                sub_and[hi_bit | mask] = sub_and[mask] & num
                sub_xor[hi_bit | mask] = sub_xor[mask] ^ num
        sub_and[0] = 0
        
        def f(sub):
            b = XorBasis(mx_bit_len)
            xor = sub_xor[sub]
            for i, num in enumerate(nums):
                if sub >> i & 1:
                    b.insert(num & ~xor)
            return xor + b.max_xor() * 2
        
        return max(sub_and[sub] + f((u - 1) ^ sub) for sub in range(u))

if __name__ == '__main__':
    s = Solution()
    print(s.maximizeXorAndXor(nums = [2,3]))
    # print(pow(2, 19))
    # print(log(10 ** 9, 2))