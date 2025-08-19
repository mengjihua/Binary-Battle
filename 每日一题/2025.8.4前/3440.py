from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations
from datetime import datetime, date, time, timedelta
from functools import cmp_to_key, lru_cache
from math import gcd, sqrt, log, ceil, floor
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
import sys
sys.setrecursionlimit(10 ** 5 + 1)

# TODO: 发题解, 复习一下
class LazyHeap:
    def __init__(self, nums):
        self.heap = []
        self.delayed = defaultdict(int)
        for x in nums:
            heappush(self.heap, -x)

    def push(self, x):
        heappush(self.heap, -x)

    def remove(self, x):
        self.delayed[-x] += 1

    def get_top2(self):
        while self.heap and self.delayed.get(self.heap[0], 0) > 0:
            x = heappop(self.heap)
            self.delayed[x] -= 1
            if self.delayed[x] == 0:
                del self.delayed[x]
        if not self.heap:
            return -10**18, -10**18
        top1 = -self.heap[0]
        x = heappop(self.heap)
        while self.heap and self.delayed.get(self.heap[0], 0) > 0:
            x2 = heappop(self.heap)
            self.delayed[x2] -= 1
            if self.delayed[x2] == 0:
                del self.delayed[x2]
        if not self.heap:
            heappush(self.heap, x)
            return top1, -10**18
        top2 = -self.heap[0]
        heappush(self.heap, x)
        return top1, top2


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        startTime, endTime = startTime + [eventTime], [0] + endTime
        # print(startTime, endTime)
        n = len(startTime)

        gaps = []
        for i in range(n):
            gaps.append(startTime[i] - endTime[i])
        first_three_gap = nlargest(3, gaps)
        # print(first_three_gap)

        # 判断是否可以用剩余的最大间隔填充, 如果不能填充, 则只考虑左边和右边的间隔
        def judge(left_gap, right_gap, length):
            remaining = first_three_gap.copy()
            if left_gap in remaining:
                remaining.remove(left_gap)
            if right_gap in remaining:
                remaining.remove(right_gap)
            # print(f'judge: {remaining}')
            if max(remaining) < length:
                return False
            return True

        ans = 0
        for i in range(1, n):
            length = endTime[i] - startTime[i - 1]
            left_gap, right_gap = startTime[i - 1] - \
                endTime[i - 1], startTime[i] - endTime[i]
            # print(f'loop{i}: {left_gap}, {right_gap}, {length}')
            if judge(left_gap, right_gap, length):
                ans = max(ans, length + left_gap + right_gap)
            else:
                ans = max(ans, left_gap + right_gap)
        return ans if ans > 0 else max(first_three_gap)

    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(endTime)
        result = 0

        ans1 = [0] * (n + 1)
        ans1[0] = startTime[0] - 0 if n > 0 else eventTime
        for i in range(1, n):
            ans1[i] = startTime[i] - endTime[i - 1]
        ans1[n] = eventTime - endTime[-1] if n > 0 else float('inf')

        ans2 = ans1.copy()
        ans1_sorted = sorted(ans1)

        for i in range(n):
            temp = endTime[i] - startTime[i]
            target_count = 0

            if temp <= ans2[i]:
                target_count += 1
            if temp <= ans2[i + 1]:
                target_count += 1

            j = len(ans1_sorted) - bisect_left(ans1_sorted, temp)

            if target_count < j:
                result = max(result, temp + ans2[i] + ans2[i + 1])
            else:
                result = max(result, ans2[i] + ans2[i + 1])

        return result

    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        n = len(startTime)
        gaps.append(startTime[0] - 0)
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i-1])
        gaps.append(eventTime - endTime[-1])

        heap = LazyHeap(gaps)
        ans = 0

        for i in range(n):
            left_gap = gaps[i]
            right_gap = gaps[i+1]
            duration = endTime[i] - startTime[i]
            new_gap_i = left_gap + right_gap + duration

            heap.remove(left_gap)
            heap.remove(right_gap)
            M1, M2 = heap.get_top2()

            option1 = -10**18
            if M1 >= duration:
                option1 = max(new_gap_i, M1 - duration, M2)
            option2 = max(new_gap_i - duration, M1)
            candidate_i = max(option1, option2)
            ans = max(ans, candidate_i)

            heap.push(left_gap)
            heap.push(right_gap)

        return ans

# if __name__ == "__main__":
#     s = Solution()
#     print(s.maxFreeTime(eventTime = 5, startTime = [1,3], endTime = [2,5]))
#     print(s.maxFreeTime(eventTime = 5, startTime = [0,1,2,3,4], endTime = [1,2,3,4,5]))
#     print(s.maxFreeTime(eventTime = 41, startTime = [17,24], endTime = [19,25]))  # 24
