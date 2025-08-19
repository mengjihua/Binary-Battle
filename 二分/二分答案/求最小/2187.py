from typing import List

class Solution:
    def check(self, x: int, times: List[int], totalTrips: int) -> int:
        return sum(x // time for time in times) >= totalTrips

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l, r = 0, min(time) * totalTrips
        while l <= r:
            mid = (l + r) // 2
            if self.check(mid, time, totalTrips):
                r = mid - 1
            else:
                l = mid + 1
        return l