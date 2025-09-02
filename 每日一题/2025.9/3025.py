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
    def numberOfPairs(self, points: List[List[int]]) -> int:
        ans = 0
        for xa, ya in points:
            for xb, yb in points:
                if xa == xb and ya == yb:
                    continue
                if xa > xb or ya < yb:
                    continue
                judge = 1
                for xc, yc in points:
                    if (xc == xa and yc == ya) or (xc == xb and yc == yb):
                        continue
                    if xa <= xc <= xb and ya >= yc >= yb:
                        judge = 0
                        break
                ans += judge
        return ans
    
    # 优化最内层循环
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # 二维前缀和记录, pre_sum[x][y]: 表示 (0,0) ~ (x,y) 范围内的点的数量
        mx_x, mx_y = max(x for x, y in points), max(y for x, y in points)
        pre_sum = [[0] * (mx_y + 2) for _ in range(mx_x + 2)]
        for x, y in points:
            pre_sum[x + 1][y + 1] += 1
        for x in range(1, mx_x + 2):
            for y in range(1, mx_y + 2):
                pre_sum[x][y] += pre_sum[x - 1][y] + pre_sum[x][y - 1] - pre_sum[x - 1][y - 1]
                
        ans = 0
        for xa, ya in points:
            for xb, yb in points:
                if xa == xb and ya == yb:
                    continue
                if xa > xb or ya < yb:
                    continue
                if pre_sum[xb + 1][ya + 1] - pre_sum[xa][ya + 1] - pre_sum[xb + 1][yb] + pre_sum[xa][yb] == 2:
                    ans += 1
        return ans
    
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: (p[0], -p[1]))
        ans = 0
        for i, (_, y1) in enumerate(points):
            max_y = -inf
            for _, y2 in points[i + 1 :]:
                if max_y < y2 <= y1:
                    max_y = y2
                    ans += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.numberOfPairs([[3,1],[1,3],[1,1]]))