from typing import List

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # set_arr = set(arr)
        # cnt = 0
        # for i in range(1, 2001):
        #     if i not in set_arr:
        #         cnt += 1
        #     if cnt == k:
        #         return i
        l, r = 0, len(arr) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, r, mid)
            if arr[mid] - (mid + 1) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return r + 1 + k