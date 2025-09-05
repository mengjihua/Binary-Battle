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

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        ''' 方法：逐轮贪心位拆分(Greedy Bit-Splitting per Step)
            思路：
              1. 模拟每一步操作: num1 -= num2
              2. 检查剩余值能否拆成 cnt 个 2 的幂
              3. 使用高位向低位贪心拆分，增加项数  '''
        cnt = 0  # 当前操作次数
        while num1 > num2:
            num1 -= num2
            cnt += 1
            num1_bit_cnt = bin(num1).count('1')
            
            if num1_bit_cnt == cnt:
                return cnt
            elif num1_bit_cnt < cnt:
                digits = [0] * 30  # digits[i]: 2^i 的个数
                digit_cnt = num1_bit_cnt  # 当前的 2^i 的个数
                
                # 初始化digits
                for i in range(29, 0, -1):
                    digits[i] = (num1 >> i) & 1
                    
                # 贪心拆分
                for i in range(29, 0, -1):
                    # while digits[i] > 0 and temp < cnt:
                    #     digits[i] -= 1
                    #     digits[i - 1] += 2
                    #     temp += 1
                    
                    # 优化: 批量拆分, 注: 不优化也能过
                    take = min(digits[i], cnt - digit_cnt)
                    digits[i] -= take
                    digits[i - 1] += take * 2
                    digit_cnt += take
                    
                    if digit_cnt == cnt:
                        return cnt
                    elif digit_cnt > cnt:
                        break
        return -1
    
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 > 0:
            num1 -= num2
            cnt += 1
            if num1.bit_count() <= cnt <= num1:
                return cnt
        return -1
    
if __name__ == "__main__":
    # print(log(10 ** 9, 2))
    s = Solution()
    print(s.makeTheIntegerZero(num1 = 3, num2 = -2))
    print(s.makeTheIntegerZero(num1 = 10 ** 9, num2 = 11))