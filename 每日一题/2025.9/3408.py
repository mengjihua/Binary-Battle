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
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7


class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.tasks = tasks
        self.task_map = {task[1]: task for task in tasks}
        self.user_tasks = defaultdict(list)
        for task in tasks:
            self.user_tasks[task[0]].append(task[1])

    def add(self, userId: int, taskId: int, priority: int) -> None:
        if taskId in self.task_map:
            self.rmv(taskId)
        self.tasks.append([userId, taskId, priority])
        self.task_map[taskId] = [userId, taskId, priority]
        self.user_tasks[userId].append(taskId)

    def edit(self, taskId: int, newPriority: int) -> None:
        if taskId in self.task_map:
            userId, _, _ = self.task_map[taskId]
            self.rmv(taskId)
            self.add(userId, taskId, newPriority)

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            userId, _, _ = self.task_map[taskId]
            self.tasks.remove(self.task_map[taskId])
            del self.task_map[taskId]
            self.user_tasks[userId].remove(taskId)

    def execTop(self) -> int:
        if not self.tasks:
            return -1
        self.tasks.sort(key=lambda x: (-x[2], x[1]))
        return self.tasks[0][1]


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()