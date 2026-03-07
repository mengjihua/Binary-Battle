from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, accumulate, pairwise
from datetime import datetime, date, time, timedelta
from time import time as timestamp, sleep
from functools import cmp_to_key, lru_cache, reduce
from math import gcd, comb, sqrt, log, ceil, floor, inf
from bisect import bisect_left, bisect_right
from heapq import heappush, heappop, heapify, nsmallest, nlargest
from sortedcontainers import SortedList
from sys import setrecursionlimit
setrecursionlimit(5 * 10 ** 5 + 1)
def fmax(a, b): return a if a > b else b
def fmin(a, b): return a if a < b else b
def lcm(a, b): return a * b // gcd(a, b)
MOD = 10 ** 9 + 7

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head: Optional['ListNode']) -> Optional['ListNode']:
    pre = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    return pre

class Solution:
    def reverseKGroup(self, head: Optional['ListNode'], k: int) -> Optional['ListNode']:
        temp = ListNode(0)
        temp.next = head
        
        pre = temp
        
        while True:
            gk = pre
            for _ in range(k):
                gk = gk.next
                if not gk:
                    return temp.next
            
            start = pre.next
            end = gk        
            nxt = end.next  
            
            end.next = None
            
            reverse(start)
            
            pre.next = end  
            start.next = nxt
            
            pre = start