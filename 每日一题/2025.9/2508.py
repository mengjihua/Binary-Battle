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

from sortedcontainers import SortedList

class Router:

    def __init__(self, memoryLimit: int):
        self.q = deque()
        self.mem = memoryLimit
        self.dic = defaultdict(int)
        self.dest = defaultdict(SortedList)
        self.cur_mem = 0

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        cur_packet = (source, destination, timestamp)
        if self.dic[cur_packet] != 0:
            return False
        if self.cur_mem == self.mem:
            old_packet = self.q.popleft()
            self.dic[old_packet] -= 1
            self.dest[old_packet[1]].remove(old_packet[2])
            self.cur_mem -= 1
        self.q.append(cur_packet)
        self.dic[cur_packet] += 1
        self.dest[destination].add(timestamp)
        self.cur_mem += 1
        return True

    def forwardPacket(self) -> List[int]:
        if not self.q:
            return []
        packet = self.q.popleft()
        self.dic[packet] -= 1
        self.dest[packet[1]].remove(packet[2])
        self.cur_mem -= 1
        return [packet[0], packet[1], packet[2]]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        lst = self.dest[destination]
        return bisect_right(lst, endTime) - bisect_left(lst, startTime)

# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)