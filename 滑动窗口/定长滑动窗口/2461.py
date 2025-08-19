from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        for i, x in enumerate(nums):
            s += x
            cnt[x] += 1

            left  = i - k + 1
            if left < 0:
                continue
            
            if len(cnt) == k:
                ans = max(ans, s)

            out = nums[left]
            s -= out
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
        return ans