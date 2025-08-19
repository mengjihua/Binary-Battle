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
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        # 定义两个变量，temp用于记录当前窗口中B的数量，tt用于记录窗口中B的最大数量
        temp, tt = 0, 0
        
        for i, color in enumerate(blocks):
            # 如果当前字符是B，则temp加1
            if color == 'B':
                temp += 1
            # 更新tt为窗口中B的最大数量
            tt = max(tt, temp)
            # 如果当前索引小于k-1，则继续循环
            if i < k - 1:
                continue
            # 如果当前索引大于等于k-1，则需要滑动窗口
            temp -= 1 if blocks[i - k + 1] == 'B' else 0
            
        # 返回需要变为B的W的数量，即k减去窗口中B的
        return k - tt if tt < k else 0
    
if __name__ == '__main__':
    s = Solution()
    print(s.minimumRecolors(blocks = "WBBWWBBWBW", k = 7))