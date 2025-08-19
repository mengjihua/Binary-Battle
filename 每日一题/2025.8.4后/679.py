from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
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
    def judgePoint24(self, cards: List[int]) -> bool:
        # 带顺序的排列组合
        combs = list(permutations(cards))
        ops = ['+', '-', '*', '/']
        def dfs(comb, i, cur, n):
            if i == n:
                return abs(cur - 24) < 1e-6
            for op in ops:
                if op == '+':
                    if dfs(comb, i + 1, cur + comb[i], n):
                        return True
                elif op == '-':
                    if dfs(comb, i + 1, cur - comb[i], n) or dfs(comb, i + 1, comb[i] - cur, n):
                        # 允许交换操作数的顺序
                        return True
                elif op == '*':
                    if dfs(comb, i + 1, cur * comb[i], n):
                        return True
                else:
                    if (comb[i] != 0 and dfs(comb, i + 1, cur / comb[i], n)) or (cur != 0 and dfs(comb, i + 1, comb[i] / cur, n)):
                        # 允许交换操作数的顺序
                        return True
            return False
        # 两者与两者之间的运算
        def cal_two(comb):
            res = False
            for op in ops:
                if op == '+':
                    num1 = comb[0] + comb[1]
                elif op == '-':
                    num1 = comb[0] - comb[1]
                elif op == '*':
                    num1 = comb[0] * comb[1]
                else:
                    num1 = comb[0] / comb[1]
                for op2 in ops:
                    if op2 == '+':
                        num2 = comb[2] + comb[3]
                    elif op2 == '-':
                        num2 = comb[2] - comb[3]
                    elif op2 == '*':
                        num2 = comb[2] * comb[3]
                    else:
                        num2 = comb[2] / comb[3]
                    res = res or dfs([num1, num2], 1, num1, 2)
            return res
                
                
        return any(dfs(comb, 1, comb[0], 4) or cal_two(comb) for comb in combs)
    
    
    def judgePoint24(self, cards: List[int]) -> bool:
        def cal(a, b):
            res = [a + b, a - b, b - a, a * b]
            if b: res.append(a / b)
            if a: res.append(b / a)
            return res
        
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < 1e-6
            # 从 nums 中选两个数进行计算
            n = len(nums)
            for i, j in combinations(range(n), 2):
                rest = [nums[k] for k in range(n) if k != i and k != j] # 剩下的数
                for num in cal(nums[i], nums[j]):
                    if dfs(rest + [num]):
                        return True
                        
            return False
        
        return dfs(cards)
    
    
if __name__ == '__main__':
    s = Solution()
    print(s.judgePoint24([1,3,4,6])) # 6 / (1 - 3 / 4) = 24
    print(s.judgePoint24([1,9,1,2])) # (9 - 1) * (2 + 1) = 24
    print(s.judgePoint24([7,2,6,6])) # (7 - (6 / 2)) * 6 = 24